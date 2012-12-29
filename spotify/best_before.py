import sys
from datetime import datetime


class BestBefore(object):
    """
    Spotify "Best Before" puzzle.
    http://www.spotify.com/uk/jobs/tech/best-before/
    """
    def __init__(self, rawinput):
        self.rawinput = rawinput

    def guess_closest_year(self, rawyear):
        """
        Given a year formatted as one, two or four
        numbers long, return a best guess what the
        user intended. For example, if this year is
        2013, and the user enters 0 or 00, 2000 would
        be returned.
        """
        closest = 3000
        rawyear = str(rawyear)
        rawlen = len(rawyear) 
        curr_year = datetime.today().year
        for year in xrange(2000, 3000):
            yearstr = str(year)
            if rawlen == 4:
                match = int(rawyear)
            else:
                diff = len(yearstr) - rawlen
                match = int(yearstr[:diff] + rawyear)
            if (closest - curr_year) > (match - curr_year):
                closest = match
        return closest

    def compute(self):
        # Split each number string and force it to an integer.
        extracted = map(lambda i: int(i), self.rawinput.split('/'))

        # Test the little endian format, day/month/year.
        little_day, little_month, raw_little_year = extracted
        little_year = self.guess_closest_year(raw_little_year)
        try:
            little_dt = datetime(little_year, little_month, little_day)
        except ValueError:
            little_dt = None

         # Test the middle endian format, month/day/year.
        middle_month, middle_day, raw_middle_year = extracted
        middle_year = self.guess_closest_year(raw_middle_year)
        try:
            middle_dt = datetime(middle_year, middle_month, middle_day)
        except ValueError:
            middle_dt = None

        # A variable to store out outputted little or
        # middle endian date, in the YYYY-MM-DD format.
        output = None

        # If we've got a little *and* middle endian date
        # to work with, only show the *earliest* date.
        if little_dt and middle_dt:
            output = little_dt
            if middle_dt < little_dt:
                output = middle_dt
        # If we've got a little endian date, print it.
        elif little_dt:
            output = little_dt
        # Otherwise, show the medium endian date.
        else:
            output = middle_dt

        if output:
            return output.strftime('%Y-%m-%d')
        else:
            return '%s is illegal' % self.rawinput


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # If we haven't got the right number
        # of args, show the usage example.
        print 'python %s {int}/{int}/{int}' % __file__
    else:
        bb = BestBefore(sys.argv[1])
        print bb.compute()
