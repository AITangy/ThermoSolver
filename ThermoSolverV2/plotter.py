from bokeh.models import Arrow, NormalHead
from bokeh.palettes import Category10
from bokeh.plotting import figure, show
from info import numberofstates
from info import accuracy
def plotaround(plotinfo,plotnumber):
    plotPv(plotinfo,plotnumber)
    ploths(plotinfo,plotnumber)
    plotTs(plotinfo,plotnumber)




#    show(plot3)

def plotPv(plotinfo,plotnumber):
    plot1 = figure(title="P v Diagram " + str(plotnumber+1), x_axis_label='v', y_axis_label='P')
    for i in range(0, numberofstates):
        plot1.line(plotinfo[i][:, 2], plotinfo[i][:, 1], legend_label="Component " + str(i), line_width=2,color=Category10[numberofstates][i])
    show(plot1)

def plotTs(plotinfo,plotnumber):
    plot2 = figure(title="T s Diagram " + str(plotnumber+1), x_axis_label='s', y_axis_label='T')
    for i in range(0, numberofstates):
        plot2.line(plotinfo[i][:, 5], plotinfo[i][:, 0], legend_label="Component " + str(i), line_width=2,color=Category10[numberofstates][i])
    show(plot2)
def ploths(plotinfo,plotnumber):
    plot3 = figure(title="h s Diagram " + str(plotnumber+1), x_axis_label='s', y_axis_label='h')
    for i in range(0, numberofstates):
        plot3.line(plotinfo[i][:, 5], plotinfo[i][:, 4], legend_label="Component " + str(i), line_width=2,color=Category10[numberofstates][i])
    show(plot3)

    print()







    # for the plotting algorythm, each time we calculagte a new quantity, we need to take the property we used and the current and previous state and store in a list a bunch of values in between prbably using numpy arrrange
    # after doing so we need to apply whatever clauclation we are using to get the values in between the values on the list to get the list of corresponding new values, we need to do thjis for each process and form eac data type.


    # There is a plotter algorythm that should be used for when isenaccounter is used to calcilate the properite shten thee is th eplotter alogrytm that should nbe ued twhen compoenent type isused to claculate the vlaues.
    # We need to seperate these two algorythms into seperate functions perhpas in the samne module anmd they should work or any vlaues.