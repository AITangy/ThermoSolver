from bokeh.models import Arrow, NormalHead
from bokeh.plotting import figure, show
from info import accuracy
def plotaround(plotinfo):
    plot1 = figure(title="Component 3", x_axis_label='v', y_axis_label='P')
    plot1.line(plotinfo[2][:,2], plotinfo[2][:,1], legend_label="Component 3", line_width=2)

    show(plot1)

    plot2 = figure(title="Component 3", x_axis_label='s', y_axis_label='T')
    plot2.line(plotinfo[2][:, 5], plotinfo[2][:, 0], legend_label="Component 3", line_width=2)

    show(plot2)

    plot3 = figure(title="Component 3", x_axis_label='s', y_axis_label='h')
    plot3.line(plotinfo[2][:, 5], plotinfo[2][:, 4], legend_label="Component 3", line_width=2)

    show(plot3)

def plotbycomponent():
    print()









    # for the plotting algorythm, each time we calculagte a new quantity, we need to take the property we used and the current and previous state and store in a list a bunch of values in between prbably using numpy arrrange
    # after doing so we need to apply whatever clauclation we are using to get the values in between the values on the list to get the list of corresponding new values, we need to do thjis for each process and form eac data type.


    # There is a plotter algorythm that should be used for when isenaccounter is used to calcilate the properite shten thee is th eplotter alogrytm that should nbe ued twhen compoenent type isused to claculate the vlaues.
    # We need to seperate these two algorythms into seperate functions perhpas in the samne module anmd they should work or any vlaues.