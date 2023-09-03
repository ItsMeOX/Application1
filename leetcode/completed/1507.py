class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": '01', 
            "Feb": '02', 
            "Mar": '03', 
            "Apr": '04',
            "May": '05', 
            "Jun": '06', 
            "Jul": '07', 
            "Aug": '08', 
            "Sep": '09', 
            "Oct": '10', 
            "Nov": '11', 
            "Dec": '12'
        }

        date = date.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')

        day, month, year = date.split(' ')

        return '{}-{}-{:02d}'.format(year, months[month], int(day))