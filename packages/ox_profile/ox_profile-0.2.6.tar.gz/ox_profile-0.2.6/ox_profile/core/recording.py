"""Module for recording and saving measurements.
"""

import re
import threading
from collections import defaultdict, Counter


RE_FILTER_ALL_CHARACTERS = '.*'


class ProfileRecord(object):
    """Simple record to track how many times a function/path is called.
    """

    def __init__(self, name, hits):
        """Initializer.

        :param name:   String name of function or stack path.

        :param hits:   Number of times it is called.
        """
        self.name = name
        self.hits = hits

    def to_str(self):
        """Return string reprsentation."""
        result = '%s(%s=%s, %s=%s)' % (
            self.__class__.__name__, 'name', self.name, 'hits', self.hits)

        return result

    def __repr__(self):
        return self.to_str()


class CountingRecorder(object):
    """Recorder which just counts how many times something is called.
    """

    def __init__(self):
        self.db_lock = threading.Lock()
        with self.db_lock:
            self.my_db = defaultdict(lambda: 0)

    def record(self, measurement):
        """Record a measurement.

        :param measurement:     An ox_profile.core.metrics.Measurement
                                for profiling the program.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        PURPOSE:  This method is called to record a measurement. Different
                  recorders may track different things about a measurement.

        """
        with self.db_lock:
            self.my_db[measurement.name] += 1

    def query(self, re_filter=RE_FILTER_ALL_CHARACTERS, max_records=10):
        """Query the database of measurements.

        :param re_filter='.*':      String regular expression for records
                                    to include in query.

        :param max_records=10:      Maximum number of records to include.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        :return:   The pair (result, count) where count num_records is the
                   total number of records in the database and result is
                   a list of ProfileRecord instances sorted to start from the
                   record with the most hits to the least with at most
                   max_records included.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        PURPOSE:   Query the database. One slightly tricky thing to keep
                   in mind here is that name of a record is the semi-colon
                   separated list of functions for the backtrace of a
                   function. To make sure to count each function call,
                   we take apart the name into the backtrace and record
                   a hit for everything in the backtrace.

        """
        if re_filter in (None, RE_FILTER_ALL_CHARACTERS):
            regexp = None
        else:
            regexp = re.compile(re_filter)
        calls_counter = Counter()
        # Lock so we don't mess with db during query.
        # *IMPORTANT: be careful in code below to not do anything to
        # call self.record or anything else which would try to acquire
        # self.db_lock otherwise you will deadlock
        with self.db_lock:
            num_records = len(self.my_db)
            # Use explicit list in case dict changes during iteration
            for name, item in list(self.my_db.items()):
                name_list = name.split(';')
                for fname in name_list:
                    if not regexp or regexp.search(fname):
                        calls_counter[fname] += item
            my_hits = calls_counter.most_common(max_records)
            result = [ProfileRecord(name, hits) for name, hits in my_hits]
            return result, num_records

    def show(self, limit=10, query=None, sep='-', col='|'):
        """Show query as pretty formatted string.

        :arg limit=10:     Maximum lines to show.

        :arg query=None:   Optional output of calling self.query()[0]. If
                           query is None, we call self.query(max_records=100)
                           to get the query.

        :arg sep='-':      Optional horizontal line separator. Use '' if
                           you do not want a separator.

        :arg col='|':      Optional vertical line separator. Use '' if
                           you do not want a separator.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        :returns:  A string with profiling results formatted nicely.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        PURPOSE:   Show the profiling results.

        """
        if query is None:
            query, num_records = self.query(max_records=100)
        else:
            num_records = len(query)
        total_hits = float(sum([item.hits for item in query]))
        if limit:
            note = '' if limit is None else (' (top %i/%i results)' % (
                min(limit, num_records), num_records))
            query = query[:limit]
        else:
            note = ''
        width = 40
        fmt = '%s {:%i} %s {:>8} %s {:>5} %s' % (col, width, col, col, col)
        header = fmt.format('Function', 'Hits', '%')
        if sep:
            line_sep = '\n  ' + (sep * len(header)) + '\n  '
        else:
            line_sep = '\n'
        text = ('Profiling results:%s\n%s' % (note, line_sep)) + (
            header + line_sep) + line_sep.join([fmt.format(
                i.name[:width], i.hits, '%.1f' % (100*(i.hits/total_hits)))
                                                  for i in query]) + line_sep

        return text
