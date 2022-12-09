import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pandas.read_csv("review_analysis/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
mnth_avg_crs = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews", classes="text-h3 text-weight-bold text-center q-pa-md inset-shadow-down shadow-1 bg-positive")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis!!!", classes="text-h3")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(mnth_avg_crs.index)
    
    hc_data =[{"name":v1, "data":[v2 for v2 in mnth_avg_crs[v1]]} for v1 in mnth_avg_crs.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)
