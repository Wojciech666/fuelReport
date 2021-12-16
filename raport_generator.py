import sys
import matplotlib.pyplot as plt
import argparse
from datetime import datetime


class InputFileOperations:
    fileLines = ""

    def __init__(self, lines):
        fileLines = lines

    def get_price_and_date_graph(self):
        prices = [line.split(":")[0] for line in self.fileLines]
        prices_list = self.change_comma_to_dot(prices)
        prices_list = self.string_to_float(prices_list)
        plot_type_label = "Gas prices zl"
        self.print_graph(prices_list, plot_type_label, "Price(date)")

    def get_total_cost_and_date_graph(self):
        total_costs = [line.split(":")[1] for line in self.fileLines]
        total_costs_list = self.change_comma_to_dot(total_costs)
        total_costs_list = self.string_to_float(total_costs_list)
        plot_type_label = "Total cost zl"
        self.print_graph(total_costs_list, plot_type_label, "TotalCost(date)")

    def get_liters_and_date_graph(self):
        liters = [line.split(":")[2] for line in self.fileLines]
        liters_list = self.change_comma_to_dot(liters)
        liters_list = self.string_to_float(liters_list)
        plot_type_label = "Liters l"
        self.print_graph(liters_list, plot_type_label, "Liters(date)")

    def get_combustion_and_date_graph(self):
        combustion_list = [line.split(":")[4] for line in self.fileLines]
        combustion_list = self.change_comma_to_dot(combustion_list)
        combustion_list = self.string_to_float(combustion_list)
        plot_type_label = "Burnout l/100km"
        self.print_graph(combustion_list, plot_type_label, "Burnout(date)")

    def change_comma_to_dot(self, list_of_data):
        result = [data.replace(",", ".") for data in list_of_data]
        return result

    def date_formater(self):
        dates = [line.split(":")[5] for line in self.fileLines]
        formated_dates = []
        for date in dates:
            formated_dates.append(date[:10])
        formated_dates = self.string_to_date(formated_dates)
        return formated_dates

    def string_to_date(self, listOfdates):
        dates_list = [datetime.strptime(date, '%d.%m.%Y').date() for date in listOfdates]
        return dates_list

    def string_to_float(self, listOfString):
        return [float(singleString) for singleString in listOfString]

    def print_graph(self, ylabel, label_text, figure_title):
        plt.plot(self.date_formater(), ylabel)
        plt.xlabel('Dates')
        plt.ylabel(f"{label_text}")
        plt.savefig(figure_title + '.png')

    def choose_graph(self, report_type):
        if report_type == 1:
            self.get_price_and_date_graph()
        elif report_type == 2:
            self.get_total_cost_and_date_graph()
        elif report_type == 3:
            self.get_liters_and_date_graph()
        elif self == 4:
            self.get_combustion_and_date_graph()
        else:
            print("nothing to print. Choose value from 1 to 4."
                  "\n1. Gas price from date graph"
                  "\n2. Total refueling price from date graph"
                  "\n3. Tanked liters from date graph"
                  "\n4. Combustion from date graph")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_in', help='input txt file with report data')
    parser.add_argument('graph_type', help='1-Gas price from date graph 2-Total refueling price from date '
                                           'graph 3 - Tanked liters from date graph 4 - Combustion from date graph')
    args = parser.parse_args()
    txt_file = args.file_in
    report_type = args.graph_type
    report_type = int(report_type)
    with open(txt_file, 'r') as uneditedReport:
        file_lines = uneditedReport.readlines()
        operations = InputFileOperations(file_lines)
        operations.choose_graph(report_type)


if __name__ == '__main__':
    main()
