import os, boto3, csv
import numpy as np
import pandas as pd

# ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
# SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# client = boto3.client('s3') #low-level functional API
# resource = boto3.resource('s3') #high-level object-oriented API
# obj = client.get_object(Bucket='gschoolcapstone', Key='npidata_20050523-20170813FileHeader.csv')
# f = obj['Body'].read().decode()
# for row in f.split('\n'):
# 	row.split(',')

my_col_names = ['NPI',
 'Entity Type Code',
#  'Replacement NPI',
#  'Employer Identification Number (EIN)',
#  'Provider Organization Name (Legal Business Name)',
#  'Provider Last Name (Legal Name)',
#  'Provider First Name',
#  'Provider Middle Name',
#  'Provider Name Prefix Text',
#  'Provider Name Suffix Text',
 'Provider Credential Text',
#  'Provider Other Organization Name',
#  'Provider Other Organization Name Type Code',
#  'Provider Other Last Name',
#  'Provider Other First Name',
#  'Provider Other Middle Name',
#  'Provider Other Name Prefix Text',
#  'Provider Other Name Suffix Text',
#  'Provider Other Credential Text',
#  'Provider Other Last Name Type Code',
#  'Provider First Line Business Mailing Address',
#  'Provider Second Line Business Mailing Address',
#  'Provider Business Mailing Address City Name',
 'Provider Business Mailing Address State Name',
 #  'Provider Business Mailing Address Postal Code',
#  'Provider Business Mailing Address Country Code (If outside U.S.)',
#  'Provider Business Mailing Address Telephone Number',
#  'Provider Business Mailing Address Fax Number',
#  'Provider First Line Business Practice Location Address',
#  'Provider Second Line Business Practice Location Address',
#  'Provider Business Practice Location Address City Name',
#  'Provider Business Practice Location Address State Name',
#  'Provider Business Practice Location Address Postal Code',
#  'Provider Business Practice Location Address Country Code (If outside U.S.)',
#  'Provider Business Practice Location Address Telephone Number',
#  'Provider Business Practice Location Address Fax Number',
#  'Provider Enumeration Date',
#  'Last Update Date',
#  'NPI Deactivation Reason Code',
 'NPI Deactivation Date',
 'NPI Reactivation Date',
 'Provider Gender Code',
#  'Authorized Official Last Name',
#  'Authorized Official First Name',
#  'Authorized Official Middle Name',
#  'Authorized Official Title or Position',
#  'Authorized Official Telephone Number',
 'Healthcare Provider Taxonomy Code_1',
#  'Provider License Number_1',
#  'Provider License Number State Code_1',
 'Healthcare Provider Primary Taxonomy Switch_1',
 'Healthcare Provider Taxonomy Code_2',
#  'Provider License Number_2',
#  'Provider License Number State Code_2',
 'Healthcare Provider Primary Taxonomy Switch_2',
 'Healthcare Provider Taxonomy Code_3',
#  'Provider License Number_3',
#  'Provider License Number State Code_3',
 'Healthcare Provider Primary Taxonomy Switch_3',
 'Healthcare Provider Taxonomy Code_4',
#  'Provider License Number_4',
#  'Provider License Number State Code_4',
 'Healthcare Provider Primary Taxonomy Switch_4',
 'Healthcare Provider Taxonomy Code_5',
#  'Provider License Number_5',
#  'Provider License Number State Code_5',
 'Healthcare Provider Primary Taxonomy Switch_5',
 'Healthcare Provider Taxonomy Code_6',
#  'Provider License Number_6',
#  'Provider License Number State Code_6',
 'Healthcare Provider Primary Taxonomy Switch_6',
 'Healthcare Provider Taxonomy Code_7',
#  'Provider License Number_7',
#  'Provider License Number State Code_7',
 'Healthcare Provider Primary Taxonomy Switch_7',
 'Healthcare Provider Taxonomy Code_8',
#  'Provider License Number_8',
#  'Provider License Number State Code_8',
 'Healthcare Provider Primary Taxonomy Switch_8',
 'Healthcare Provider Taxonomy Code_9',
#  'Provider License Number_9',
#  'Provider License Number State Code_9',
 'Healthcare Provider Primary Taxonomy Switch_9',
 'Healthcare Provider Taxonomy Code_10',
#  'Provider License Number_10',
#  'Provider License Number State Code_10',
 'Healthcare Provider Primary Taxonomy Switch_10',
 'Healthcare Provider Taxonomy Code_11',
#  'Provider License Number_11',
#  'Provider License Number State Code_11',
 'Healthcare Provider Primary Taxonomy Switch_11',
 'Healthcare Provider Taxonomy Code_12',
#  'Provider License Number_12',
#  'Provider License Number State Code_12',
 'Healthcare Provider Primary Taxonomy Switch_12',
 'Healthcare Provider Taxonomy Code_13',
#  'Provider License Number_13',
#  'Provider License Number State Code_13',
 'Healthcare Provider Primary Taxonomy Switch_13',
 'Healthcare Provider Taxonomy Code_14',
#  'Provider License Number_14',
#  'Provider License Number State Code_14',
 'Healthcare Provider Primary Taxonomy Switch_14',
 'Healthcare Provider Taxonomy Code_15',
#  'Provider License Number_15',
#  'Provider License Number State Code_15',
 'Healthcare Provider Primary Taxonomy Switch_15',
#  'Other Provider Identifier_1',
#  'Other Provider Identifier Type Code_1',
#  'Other Provider Identifier State_1',
#  'Other Provider Identifier Issuer_1',
#  'Other Provider Identifier_2',
#  'Other Provider Identifier Type Code_2',
#  'Other Provider Identifier State_2',
#  'Other Provider Identifier Issuer_2',
#  'Other Provider Identifier_3',
#  'Other Provider Identifier Type Code_3',
#  'Other Provider Identifier State_3',
#  'Other Provider Identifier Issuer_3',
#  'Other Provider Identifier_4',
#  'Other Provider Identifier Type Code_4',
#  'Other Provider Identifier State_4',
#  'Other Provider Identifier Issuer_4',
#  'Other Provider Identifier_5',
#  'Other Provider Identifier Type Code_5',
#  'Other Provider Identifier State_5',
#  'Other Provider Identifier Issuer_5',
#  'Other Provider Identifier_6',
#  'Other Provider Identifier Type Code_6',
#  'Other Provider Identifier State_6',
#  'Other Provider Identifier Issuer_6',
#  'Other Provider Identifier_7',
#  'Other Provider Identifier Type Code_7',
#  'Other Provider Identifier State_7',
#  'Other Provider Identifier Issuer_7',
#  'Other Provider Identifier_8',
#  'Other Provider Identifier Type Code_8',
#  'Other Provider Identifier State_8',
#  'Other Provider Identifier Issuer_8',
#  'Other Provider Identifier_9',
#  'Other Provider Identifier Type Code_9',
#  'Other Provider Identifier State_9',
#  'Other Provider Identifier Issuer_9',
#  'Other Provider Identifier_10',
#  'Other Provider Identifier Type Code_10',
#  'Other Provider Identifier State_10',
#  'Other Provider Identifier Issuer_10',
#  'Other Provider Identifier_11',
#  'Other Provider Identifier Type Code_11',
#  'Other Provider Identifier State_11',
#  'Other Provider Identifier Issuer_11',
#  'Other Provider Identifier_12',
#  'Other Provider Identifier Type Code_12',
#  'Other Provider Identifier State_12',
#  'Other Provider Identifier Issuer_12',
#  'Other Provider Identifier_13',
#  'Other Provider Identifier Type Code_13',
#  'Other Provider Identifier State_13',
#  'Other Provider Identifier Issuer_13',
#  'Other Provider Identifier_14',
#  'Other Provider Identifier Type Code_14',
#  'Other Provider Identifier State_14',
#  'Other Provider Identifier Issuer_14',
#  'Other Provider Identifier_15',
#  'Other Provider Identifier Type Code_15',
#  'Other Provider Identifier State_15',
#  'Other Provider Identifier Issuer_15',
#  'Other Provider Identifier_16',
#  'Other Provider Identifier Type Code_16',
#  'Other Provider Identifier State_16',
#  'Other Provider Identifier Issuer_16',
#  'Other Provider Identifier_17',
#  'Other Provider Identifier Type Code_17',
#  'Other Provider Identifier State_17',
#  'Other Provider Identifier Issuer_17',
#  'Other Provider Identifier_18',
#  'Other Provider Identifier Type Code_18',
#  'Other Provider Identifier State_18',
#  'Other Provider Identifier Issuer_18',
#  'Other Provider Identifier_19',
#  'Other Provider Identifier Type Code_19',
#  'Other Provider Identifier State_19',
#  'Other Provider Identifier Issuer_19',
#  'Other Provider Identifier_20',
#  'Other Provider Identifier Type Code_20',
#  'Other Provider Identifier State_20',
#  'Other Provider Identifier Issuer_20',
#  'Other Provider Identifier_21',
#  'Other Provider Identifier Type Code_21',
#  'Other Provider Identifier State_21',
#  'Other Provider Identifier Issuer_21',
#  'Other Provider Identifier_22',
#  'Other Provider Identifier Type Code_22',
#  'Other Provider Identifier State_22',
#  'Other Provider Identifier Issuer_22',
#  'Other Provider Identifier_23',
#  'Other Provider Identifier Type Code_23',
#  'Other Provider Identifier State_23',
#  'Other Provider Identifier Issuer_23',
#  'Other Provider Identifier_24',
#  'Other Provider Identifier Type Code_24',
#  'Other Provider Identifier State_24',
#  'Other Provider Identifier Issuer_24',
#  'Other Provider Identifier_25',
#  'Other Provider Identifier Type Code_25',
#  'Other Provider Identifier State_25',
#  'Other Provider Identifier Issuer_25',
#  'Other Provider Identifier_26',
#  'Other Provider Identifier Type Code_26',
#  'Other Provider Identifier State_26',
#  'Other Provider Identifier Issuer_26',
#  'Other Provider Identifier_27',
#  'Other Provider Identifier Type Code_27',
#  'Other Provider Identifier State_27',
#  'Other Provider Identifier Issuer_27',
#  'Other Provider Identifier_28',
#  'Other Provider Identifier Type Code_28',
#  'Other Provider Identifier State_28',
#  'Other Provider Identifier Issuer_28',
#  'Other Provider Identifier_29',
#  'Other Provider Identifier Type Code_29',
#  'Other Provider Identifier State_29',
#  'Other Provider Identifier Issuer_29',
#  'Other Provider Identifier_30',
#  'Other Provider Identifier Type Code_30',
#  'Other Provider Identifier State_30',
#  'Other Provider Identifier Issuer_30',
#  'Other Provider Identifier_31',
#  'Other Provider Identifier Type Code_31',
#  'Other Provider Identifier State_31',
#  'Other Provider Identifier Issuer_31',
#  'Other Provider Identifier_32',
#  'Other Provider Identifier Type Code_32',
#  'Other Provider Identifier State_32',
#  'Other Provider Identifier Issuer_32',
#  'Other Provider Identifier_33',
#  'Other Provider Identifier Type Code_33',
#  'Other Provider Identifier State_33',
#  'Other Provider Identifier Issuer_33',
#  'Other Provider Identifier_34',
#  'Other Provider Identifier Type Code_34',
#  'Other Provider Identifier State_34',
#  'Other Provider Identifier Issuer_34',
#  'Other Provider Identifier_35',
#  'Other Provider Identifier Type Code_35',
#  'Other Provider Identifier State_35',
#  'Other Provider Identifier Issuer_35',
#  'Other Provider Identifier_36',
#  'Other Provider Identifier Type Code_36',
#  'Other Provider Identifier State_36',
#  'Other Provider Identifier Issuer_36',
#  'Other Provider Identifier_37',
#  'Other Provider Identifier Type Code_37',
#  'Other Provider Identifier State_37',
#  'Other Provider Identifier Issuer_37',
#  'Other Provider Identifier_38',
#  'Other Provider Identifier Type Code_38',
#  'Other Provider Identifier State_38',
#  'Other Provider Identifier Issuer_38',
#  'Other Provider Identifier_39',
#  'Other Provider Identifier Type Code_39',
#  'Other Provider Identifier State_39',
#  'Other Provider Identifier Issuer_39',
#  'Other Provider Identifier_40',
#  'Other Provider Identifier Type Code_40',
#  'Other Provider Identifier State_40',
#  'Other Provider Identifier Issuer_40',
#  'Other Provider Identifier_41',
#  'Other Provider Identifier Type Code_41',
#  'Other Provider Identifier State_41',
#  'Other Provider Identifier Issuer_41',
#  'Other Provider Identifier_42',
#  'Other Provider Identifier Type Code_42',
#  'Other Provider Identifier State_42',
#  'Other Provider Identifier Issuer_42',
#  'Other Provider Identifier_43',
#  'Other Provider Identifier Type Code_43',
#  'Other Provider Identifier State_43',
#  'Other Provider Identifier Issuer_43',
#  'Other Provider Identifier_44',
#  'Other Provider Identifier Type Code_44',
#  'Other Provider Identifier State_44',
#  'Other Provider Identifier Issuer_44',
#  'Other Provider Identifier_45',
#  'Other Provider Identifier Type Code_45',
#  'Other Provider Identifier State_45',
#  'Other Provider Identifier Issuer_45',
#  'Other Provider Identifier_46',
#  'Other Provider Identifier Type Code_46',
#  'Other Provider Identifier State_46',
#  'Other Provider Identifier Issuer_46',
#  'Other Provider Identifier_47',
#  'Other Provider Identifier Type Code_47',
#  'Other Provider Identifier State_47',
#  'Other Provider Identifier Issuer_47',
#  'Other Provider Identifier_48',
#  'Other Provider Identifier Type Code_48',
#  'Other Provider Identifier State_48',
#  'Other Provider Identifier Issuer_48',
#  'Other Provider Identifier_49',
#  'Other Provider Identifier Type Code_49',
#  'Other Provider Identifier State_49',
#  'Other Provider Identifier Issuer_49',
#  'Other Provider Identifier_50',
#  'Other Provider Identifier Type Code_50',
#  'Other Provider Identifier State_50',
#  'Other Provider Identifier Issuer_50',
 'Is Sole Proprietor',
 'Is Organization Subpart',
#  'Parent Organization LBN',
#  'Parent Organization TIN',
#  'Authorized Official Name Prefix Text',
#  'Authorized Official Name Suffix Text',
#  'Authorized Official Credential Text'
       ]

class NPIparser(object):

	def __init__ (self):
		self.code_dict = self._create_code_dict()
		self.codes = np.array([code for code in self.code_dict.keys()])
		self.states = np.array(['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', \
								'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', \
								'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', \
								'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', \
								'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'])

	def _create_code_dict(self):
		code_file = 'data/nucc_taxonomy_171.csv'
		code_f = open(code_file, 'r')
		code_reader = csv.reader(code_f)
		code_header = next(code_reader) # ['Code', 'Grouping', 'Classification', 'Specialization', 'Definition', 'Notes']
		code_dict = {line[0]: line[1:] for line in code_reader}
		code_f.close()
		return code_dict

	def parse_to_numeric(self, filename):
		file_in = open(filename, 'r')
		reader = csv.reader(file_in)
		header = next(reader)

		file_out = open('clean_data.csv', 'w')
		writer = csv.writer(file_out)

		self._write_header(writer, header) # Write header with new columns
		self._line_by_line(reader, writer)

		file_in.close()
		file_out.close()
		return 'File has been parsed.'

	def _write_header(self, writer, header):
		self.h_cols = [0,   1,  10,  23,  39,  40,  41,  47,  50,  51,  54,  55,  58,
				59,  62,  63,  66,  67,  70,  71,  74,  75,  78,  79,  82,  83,
				86,  87,  90,  91,  94,  95,  98,  99, 102, 103, 106, 307, 308]
		col_names = np.array(header)[self.h_cols]
		# col_names.append('Primary Taxonomy Code')
		col_names = np.append(col_names, self.codes)	# Add column for each Taxonomy Code
		col_names = np.append(col_names, self.states)	# Add column for each state

		writer.writerow(col_names.tolist())
		return None

	def _line_by_line(self, reader, writer):
		self.l_cols = [0,   1,  10,  23,  39,  40,  41,  47,  50,  51,  54,  55,  58,
				59,  62,  63,  66,  67,  70,  71,  74,  75,  78,  79,  82,  83,
				86,  87,  90,  91,  94,  95,  98,  99, 102, 103, 106, 307, 308]
		for i,line in enumerate(reader):
			if np.array(line)[1] != '': # only include NPI if Entity Type is not empty
				line_items = np.array(line)[self.l_cols]

				specialties = self._find_specialties(line_items, self.codes)
				line_items = np.append(line_items, specialties)

				states = self._find_states(line_items, self.states)
				line_items = np.append(line_items, states)

				# print(line_items)
				writer.writerow(line_items)
			if i%1000==0 and i!=0: print(i)
			if i==0: break
		return None

	# def find_primary(self, line):
	# 	cols = np.arange(8,38,2)
	# 	idx = cols[(line[cols] == 'Y').argmax()] - 1
	# 	return line[idx] # Returns code that is primary

	def _find_specialties(self, line, codes):
		has = line[np.arange(7,37,2)]
		return np.in1d(codes, has).astype(int)

	def _find_states(self, line, states):
		has = line[3]
		return np.in1d(states, has).astype(int)





if __name__ == '__main__':

	npi = NPIparser()
	npi_file = 'data/npidata_20050523-20170813.csv'
	npi.parse_to_numeric(npi_file)

	df = pd.read_csv('clean_data.csv')
