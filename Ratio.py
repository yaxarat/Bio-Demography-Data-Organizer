import glob
import re
import os
import pandas as pd

folder_path = []
file_path = []
parent_path = "D:\Yashar\Programming Projects\Projects\SM-data-organizer\separated_records"
age_of_death = []
count = []
population = 0


def get_path():
    global folder_path, file_path

    for filename in glob.iglob(parent_path + '/**/*.txt', recursive=True):
        file_path.append(filename)
        strain_name = (re.search(r'(?<=\\)(.*)(?=.txt)', filename)).group()
        folder_path.append(strain_name)

    print(folder_path)
    print(file_path)


def create_work_space():
    global age_of_death, count, population
    index = 0

    for path in file_path:
        print(path)
        with open(path) as data_file:
            data = data_file.readline()
            while data:
                age_of_death.append(data.strip('\n').split('\t')[2])
                data = data_file.readline()
        mortfraq_path = "freqfrq/{}/{}/".format(str(folder_path[index])[84:], "mortfraq")
        mortfreq_path = "freqfrq/{}/{}/".format(str(folder_path[index])[84:], "mortfreq")
        survfraq_path = "freqfrq/{}/{}/".format(str(folder_path[index])[84:], "survfraq")
        survfreq_path = "freqfrq/{}/{}/".format(str(folder_path[index])[84:], "survfreq")
        os.makedirs(os.path.dirname(mortfraq_path), exist_ok=True)
        os.makedirs(os.path.dirname(mortfreq_path), exist_ok=True)
        os.makedirs(os.path.dirname(survfraq_path), exist_ok=True)
        os.makedirs(os.path.dirname(survfreq_path), exist_ok=True)
        population = len(age_of_death)
        freq_table(mortfreq_path, survfreq_path, mortfraq_path, survfraq_path)
        age_of_death = []
        count = []
        population = 0
        index += 1


def freq_table(mort_freq, surv_freq, mort_fraq, surv_fraq):
    data_frame = pd.DataFrame({'age_of_death': age_of_death})
    data_frame = pd.value_counts(data_frame.age_of_death).to_frame().reset_index()
    data_frame.columns = ['age_of_death', 'count']
    data_frame.sort_values('age_of_death', inplace=True)

    to_list(data_frame, mort_freq, surv_freq, mort_fraq, surv_fraq)


def to_list(data_frame, mort_freq, surv_freq, mort_fraq, surv_fraq):
    global age_of_death, count
    current_population = population
    mortfreq_file = open("{}/{}".format(mort_freq, "strain.mortfreq"), 'w+')
    mortfreq_file.write("{}\t{}\n".format(0, 0))
    survfreq_file = open("{}/{}".format(surv_freq, "strain.survfreq"), 'w+')
    survfreq_file.write("{}\t{}\n".format(0, population))
    age_of_death = data_frame["age_of_death"].values.tolist()
    count = data_frame["count"].values.tolist()

    for index in range(len(age_of_death)):
        current_population -= count[index]
        mortfreq_file.write('%s\t%s\n' % (age_of_death[index], count[index]))
        survfreq_file.write('%s\t%s\n' % (age_of_death[index], current_population))

    fraq_table(mort_fraq, surv_fraq)


def fraq_table(mort_fraq, surv_fraq):
    current_population = population
    mortfraq_file = open("{}/{}".format(mort_fraq, "strain.mortfraq"), 'w+')
    mortfraq_file.write('{}\t{}\n'.format(0, 0))
    survfraq_file = open("{}/{}".format(surv_fraq, "strain.survfraq"), 'w+')
    survfraq_file.write("{}\t{}/{}\n".format(0, population, population))

    for index in range(len(age_of_death)):
        current_population -= count[index]
        mortfraq_file.write('%s\t%s\n' % (age_of_death[index], '{}/{}'.format(count[index], population)))
        survfraq_file.write('%s\t%s\n' % (age_of_death[index], '{}/{}'.format(current_population, population)))


get_path()
create_work_space()