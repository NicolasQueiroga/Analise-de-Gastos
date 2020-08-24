import pandas as pd
import numpy as np


class Df:

    def __init__(self, dates, categories, titles, amounts):
        self.df = pd.read_excel('Gastos.xlsx')
        self.date = dates
        self.category = categories
        self.title = titles
        self.amount = amounts

    def adiciona_transacao(self):
        new_data = pd.DataFrame({'date': self.date, 'category': self.category, 'title': self.title, 'amount': self.amount})
        self.df = self.df.append(new_data)
        self.df = self.df.sort_values(by='date', ascending=True, ignore_index=True)
        return self.df.to_excel('Gastos.xlsx', index=False)

    def adiciona_extrato(self, fileName):
        new_data = pd.read_csv(fileName)
        new_data = new_data[~(new_data['amount'] <= 0)]
        self.df = self.df.append(new_data)
        self.df = self.df.sort_values(by='date', ascending=True, ignore_index=True)
        return self.df.to_excel('Gastos.xlsx', index=False)