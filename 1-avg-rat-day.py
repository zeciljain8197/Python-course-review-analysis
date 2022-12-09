import justpy as jp
import pandas as p
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Data object created to fetch data from csv file stored in the system

data = p.read_csv("review_analysis/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date 
day_avg = data.groupby(['Day']).mean()

# For inserting charts and graphs we can visit Highcharts website and browse its library for the same.
# This object has the code of "spline" chart which was taken from the Highcharts website.
"""Note: the spline chart is customizable
        We can either make changes in the dictionary of the spline chart
        Or we can fetch the info of the dictionary in the code below and make necessary changes there as well.
"""
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Course by Day'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

# The method defined for creation of web app using justpy library
def app():
    
    # Here we have created a "wp" object for website using justpy's QuasarPage method
    wp = jp.QuasarPage()
    
    # Here we have created a div wherein we are adding a text block which will be shown on the top of the page
    """ 
    - We can format the div as per out requirement using classes attribute
    - We need to keep in mind the order of addition of div blocks as they will be shown in the same order as they are 
      defined here.    
    """
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews", classes="text-h3 text-weight-bold text-center q-pa-md inset-shadow-down shadow-1 bg-positive")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis!!!", classes="text-h3")
    
    # Here we have used Highcharts method to add charts in the web app 
    # Highcharts method takes in a options arguments where we need to pass the var created for the chart  
    hc = jp.HighCharts(a=wp, options=chart_def)

    # Here we are adding a categories key to xAxis key in spline chart's dictionary for inserting our
    # data in place of the any existing data present in the dictionary.
    hc.options.xAxis.categories = list(day_avg.index)

    # Here we are fetching the series key of the dictionary and passing our own values in the form of list which is required 
    hc.options.series[0].data = list(day_avg['Rating'])
    hc.options.title.text = 'Average Rating by Day'
    hc.options.yAxis.title.text = 'Ratings'
    hc.options.xAxis.title.text = 'Dates'
    return wp

# justpy takes in a method so we just need to pass the method name without parenthesis. 
jp.justpy(app)

