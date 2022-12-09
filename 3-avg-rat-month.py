import justpy as jp
import pandas as p
from datetime import datetime
from pytz import utc


data = p.read_csv("review_analysis/reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m') 
mnth_avg = data.groupby(['Month']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Course by Month'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'MOnth'
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
}"""

def app():

    wp = jp.QuasarPage()
    
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews", classes="text-h3 text-weight-bold text-center q-pa-md inset-shadow-down shadow-1 bg-positive")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis!!!", classes="text-h3")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(mnth_avg.index)
    hc.options.series[0].data = list(mnth_avg['Rating'])

    return wp

jp.justpy(app)

