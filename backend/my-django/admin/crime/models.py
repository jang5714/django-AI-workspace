import pandas as pd
from django.db import models
from icecream import ic

from admin.common.models import ValueObject, Reader, Printer


class CrimeCctvModel(object):
    vo = ValueObject()
    reader = Reader()
    printer = Printer()

    def __init__(self):
        '''
        Raw Data 의 features 를 가져온다.
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.vo.context = 'admin/crime/data/'
        self.crime_columns = ['살인발생', '강도발생', '강간발생', '절도발생', '폭력발생'] # Nominal
        self.arrest_columns = ['살인검거', '강도검거', '강간검거', '절도검거', '폭력검거'] # Nominal
        self.arrest_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율'] # Ratio

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        print(f'파일명: {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        self.printer.dframe(crime_model)
        return crime_model

    def create_police_position(self) -> object:
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        [station_names.append('서울' + str(name[:-1] + '경찰서')) for name in crime['관서명']]
        station_addrs = []
        station_late = []
        station_lngs =[]
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_addrs.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_late.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        # crime.to_csv(self.vo.context+'new_data/police_positions.csv')
        return crime

    def create_cctv_model(self) -> object:
        vo = self.vo
        reader = self.reader
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        print(f'파일명: {cctv_file_name}')
        cctv_model = reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명':'구별'}, inplace=True)
        # 하나의 columns을 바꿀때 사용
        self.printer.dframe(cctv_model)
        cctv_model.to_csv(self.vo.context + 'new_data/new_cctv.csv')
        return cctv_model

    def create_population_model(self) -> object:
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.fname = '01. population_in_Seoul'
        population_file_name = reader.new_file(vo)
        print(f'파일명: {population_file_name}')
        population_model = reader.xls(population_file_name, 2, 'B,D,G,J,N')
        population_model.columns = ['구별','인구수','한국인','외국인','고령자']
        #위에서 컬럼을 지정해 주었기 때문에 한꺼번에 바꾸면 된다.
        population_model.drop([26], inplace=True)
        printer.dframe(population_model)
        population_model.to_csv(self.vo.context + 'new_data/new_pop02.csv')
        return population_model

    def merge_cctv_pop(self):
        cctv_model = self.create_cctv_model()
        pop_model = self.create_population_model()
        cctv_pop_model = pd.merge(cctv_model,pop_model)
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''

        ic(cctv_pop_model.corr())
        '''
                             소계    2013년도 이전   2014년  2015년    2016년     인구수    한국인     외국인      고령자
           소계            1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
           2013년도 이전    0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
           2014년          0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
           2015년          0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
           2016년          0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
           인구수          [0.306342]   0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
           한국인          [0.304287]   0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
           외국인          [-0.023786]  0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
           고령자          [0.255196]   0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000

        '''
        self.printer.dframe(cctv_pop_model)
        # cctv_pop_model.to_csv(self.vo.context + 'new_data/new_cctv_pop.csv')

    def sum_crime(self):

        vo = self.vo
        vo.context = 'admin/crime/data/new_data/'
        reader = self.reader
        vo.fname = 'police_positions'
        cctv_file_name = reader.new_file(vo)
        print(f'파일명: {cctv_file_name}')
        crime = reader.csv(cctv_file_name)
        crime['범죄 발생'] = crime.loc['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생'].sum(axis=1)
        # crime['범죄 검거'] = crime.loc[:, [3, 6, 8, 10, 12]].sum(axis=1)
        # crime_final = crime.drop([crime.columns[0]],axis=1)
        # crime.drop(crime.columns[2], crime.columns[11])

        # crime['범죄 검거'] = crime.loc[:'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'].sum()
        # self.printer.dframe(crime)
        crime.to_csv('admin/crime/data/' + 'new_data/new_crime01.csv')
