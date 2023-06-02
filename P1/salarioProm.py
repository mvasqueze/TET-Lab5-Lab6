from mrjob.job import MRJob

class SalaryAverage(MRJob):

    def mapper(self, _, line):
        idemp, _, salario = line.split(',')
        yield idemp, float(salario)

    def reducer(self, key, values):
        total_salarios = 0
        count = 0

        for salario in values:
            total_salarios += salario
            count += 1

        yield key, total_salarios / count

if __name__ == '__main__':
    SalaryAverage.run()
