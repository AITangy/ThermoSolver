from bokeh.models import Arrow, NormalHead
from bokeh.palettes import Category10
from bokeh.plotting import figure, show
from bokeh.layouts import row,widgetbox,layout
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from info import numberofstates,dpnum
from info import accuracy
import numpy as np
def plotaround(plotinfo,plotnumber,processes):
    plot1 = plotPv(plotinfo,plotnumber,processes)
    plot2 = ploths(plotinfo,plotnumber,processes)
    plot3 = plotTs(plotinfo,plotnumber,processes)
    return plot1,plot2,plot3



#    show(plot3)

def plotPv(plotinfo,plotnumber,processes):
    plot1 = figure(title="P v Diagram " + str(plotnumber+1), x_axis_label='v(m^3/kg)', y_axis_label='P(Pa)')
    for i in range(0, numberofstates):
        plot1.line(plotinfo[i][:, 2], plotinfo[i][:, 1], legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])

    plot1.add_layout(plot1.legend[0], 'right')
    return plot1

def plotTs(plotinfo,plotnumber,processes):
    plot2 = figure(title="T s Diagram " + str(plotnumber+1), x_axis_label='s(J/(Kg*K)', y_axis_label='T(K)')
    for i in range(0, numberofstates):
        plot2.line(plotinfo[i][:, 5], plotinfo[i][:, 0], legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])

    plot2.add_layout(plot2.legend[0], 'right')
    return plot2
def ploths(plotinfo,plotnumber,processes):
    plot3 = figure(title="h s Diagram " + str(plotnumber+1), x_axis_label='s(J/(Kg*K)', y_axis_label='h(J)')
    for i in range(0, numberofstates):
        plot3.line(plotinfo[i][:, 5], plotinfo[i][:, 4], legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])

    plot3.add_layout(plot3.legend[0], 'right')
    return plot3

def plotaroundundefined(plotinfo,plotnumber,processes):

    plot1 =plotPvundefined(plotinfo,plotnumber,processes)
    plot2 = plothsundefined(plotinfo,plotnumber,processes)
    plot3 = plotTsundefined(plotinfo,plotnumber,processes)
    return plot1,plot2,plot3

def defmessage(definedstates, properties,plotinfo,plotnumber,processes):
    found = True


    # Temperatures = {i : properties[i,0] for i in range(0,numberofstates)}
    # Pressures = {i: properties[i, 1] for i in range(0, numberofstates)}
    # Volumes = {i: properties[i, 2] for i in range(0, numberofstates)}
    # InternalEnergies ={i: properties[i, 3] for i in range(0, numberofstates)}
    # Enthalipes = {i: properties[i, 4] for i in range(0, numberofstates)}
    # Entropies = {i: properties[i, 5] for i in range(0, numberofstates)}
    #
    columns = [
        TableColumn(field="Temperatures", title="T(K)"),
        TableColumn(field="Pressures", title="Pressure(Pa)"),
        TableColumn(field="Volumes",title="v(m^3/kg)"),
        TableColumn(field = "InternalEnergies", title= "u(J/kg)"),
        TableColumn(field = "Enthalpies", title= "h(J/kg)"),
        TableColumn(field = "Entropies", title="s(J/(kg*K)")
    ]
    roundedproperties = np.round(properties, decimals=dpnum, out=None)

    data = {'Temperatures': roundedproperties[:,0],
            'Pressures': roundedproperties[:,1],
            'Volumes':roundedproperties[:,2],
            'InternalEnergies':roundedproperties[:,3],
            'Enthalpies':roundedproperties[:,4],
            'Entropies':roundedproperties[:,5]}

    source = ColumnDataSource(data=data)
    print(data)
    print(processes)
    data_table = DataTable(source=source, columns=columns, width=2000, height=1000)
    for i in range(0, numberofstates):
        if definedstates[i] == False:
            found = False
    if found == False:
        print("Enough information was not provided to solve the system")
        plot1,plot2,plot3 =plotaroundundefined(plotinfo,plotnumber,processes)
    else:
        print("System was solved with the following properties:")
        print(properties)
        plot1,plot2,plot3= plotaround(plotinfo,plotnumber,processes)


    show(layout([
    [plot1,plot2,plot3],
    [data_table],
]))

def plotPvundefined(plotinfo, plotnumber, processes):
    plot1 = figure(title="P v Diagram " + str(plotnumber + 1), x_axis_label='v(m^3/kg)', y_axis_label='P(Pa)')
    for i in range(0, numberofstates):
        plot1.scatter(plotinfo[i][:, 2], plotinfo[i][:, 1],legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])
    plot1.add_layout(plot1.legend[0], 'right')
    return plot1

def plotTsundefined(plotinfo, plotnumber, processes):
    plot2 = figure(title="T s Diagram " + str(plotnumber + 1), x_axis_label='s(J/(Kg*K)', y_axis_label='T(K)')
    for i in range(0, numberofstates):
        plot2.scatter(plotinfo[i][:, 5], plotinfo[i][:, 0],legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])

    plot2.add_layout(plot2.legend[0], 'right')
    return plot2

def plothsundefined(plotinfo, plotnumber, processes):
    plot3 = figure(title="h s Diagram " + str(plotnumber + 1), x_axis_label='s(J/(Kg*K)', y_axis_label='T(K)')
    for i in range(0, numberofstates):
        plot3.scatter(plotinfo[i][:, 5], plotinfo[i][:, 4],legend_label="Component " + str(i) + " " + str(processes[i][5]), line_width=2,color=Category10[numberofstates][i])
    plot3.add_layout(plot3.legend[0], 'right')
    return plot3





    # for the plotting algorythm, each time we calculagte a new quantity, we need to take the property we used and the current and previous state and store in a list a bunch of values in between prbably using numpy arrrange
    # after doing so we need to apply whatever clauclation we are using to get the values in between the values on the list to get the list of corresponding new values, we need to do thjis for each process and form eac data type.


    # There is a plotter algorythm that should be used for when isenaccounter is used to calcilate the properite shten thee is th eplotter alogrytm that should nbe ued twhen compoenent type isused to claculate the vlaues.
    # We need to seperate these two algorythms into seperate functions perhpas in the samne module anmd they should work or any vlaues.