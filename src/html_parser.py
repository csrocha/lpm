import bs4
import pandas
import entry


class Parse(object):
    SOURCE_SYSTEM       = 'Source System'
    FUNCTION            = 'Function'
    ERROR_TYPE          = 'Error Type'
    DATE                = 'Date'
    MESSAGE             = 'Message'
    COMMENTS            = 'Comments'

    def __init__(self, html):
        self.parse = bs4.BeautifulSoup(content, features="html.parser")
        self.dataframe = pandas.DataFrame(columns=[Parse.SOURCE_SYSTEM,
                                                   Parse.FUNCTION,
                                                   Parse.ERROR_TYPE,
                                                   Parse.DATE,
                                                   Parse.MESSAGE,
                                                   Parse.COMMENTS],
                                          index=None)

    def _get_feed_table(self):
        labels = self.parse.find_all('font', recursive=True)

        for current_label in labels:
            if current_label.text == 'Feed Logfile Errors':
                # label found. Getting sibling which is the table which I' looking for
                table_element = current_label.find_next_sibling('table')

                # getting rows
                rows = table_element.findAll('tr')

                first = True
                for row in rows:
                    if first:
                        first = False
                        continue

                    df_row = pandas.DataFrame(columns=self.dataframe.columns,
                                              index=None)

                    cols = row.findAll('td')

                    (function, date, error_type, msg, comments) = tuple([str(col.find(text=True)) for col in cols])

                    df_row.loc[0] = ['PTP',
                                     function,
                                     error_type,
                                     date,
                                     msg,
                                     comments]
                    self.dataframe = self.dataframe.append(df_row)

                break

    def entries(self):
        # populating the feed table

        self._get_feed_table()

        # creating the Entry List
        return [entry.Entry(system='PTP',
                            function=row[Parse.FUNCTION],
                            date=row[Parse.DATE],
                            message=row[Parse.MESSAGE],
                            comments=row[Parse.COMMENTS],
                            keywords=[row[Parse.ERROR_TYPE]]) for row in self.dataframe.iterrows()]



if __name__ == '__main__':
    with open('/Volumes/DATA/hackathon/msg.xml') as file_content:
        content = ''
        for line in file_content.readlines():
            content += line + '\n'

    parser = Parse(content)
    parser._get_feed_table()
    print parser.dataframe.to_string()

