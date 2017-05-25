import csv

paramlist = []
filename = 'all_parameter_cd_query.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for n, row in enumerate(reader):
        if n < 9:
            continue
        elif 'water' not in row[2]:
            continue
        else:
            paramlist.append(row)

rank0 = list(set([p[1] for p in paramlist]))
rank0.sort()

inorganics_major_metals = [p for p in paramlist
                           if p[1] == 'Inorganics, Major, Metals']
inorganics_major_metal_names = set([p[2].split(',')[0] for p in inorganics_major_metals])

inorganics_minor_metals = [p for p in paramlist
                           if p[1] == 'Inorganics, Minor, Metals']
inorganics_minor_metal_names = set([p[2].split(',')[0] for p in inorganics_minor_metals])

inorganics_major_non_metals = [p for p in paramlist
                               if p[1] == 'Inorganics, Major, Non-metals']
inorganics_major_non_metals_names = set([p[2].split(',')[0] for p in inorganics_major_non_metals])


