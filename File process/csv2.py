#CREATE SUMMARY REPORT OF SUBJECTS AND NUMBER OF STUDENTS. WRITE TO CSV FILE
import csv

class Report_generator:
    def __init__(self):
        self.exam_name = []
        self.candidate_id = []
        self.score = []
        self.grade = []
        self.results = {"Maths":[0,0,0,0,100],"Physics":[0,0,0,0,100],"Biology":[0,0,0,0,100]}

    def open_file(self, file_name = 'exam_results.csv'):
        with open(file_name, newline = '') as csvfile:
            file_reader = csv.DictReader(csvfile,delimiter = ',')
            for row in file_reader:
                self.exam_name.append(row['Exam Name'])
                self.candidate_id.append(row['Candidate ID'])
                self.score.append(row['Score'])
                self.grade.append(row['Grade'])

    def create_table(self):
        unique_subjects = list(set(self.exam_name))
        unique_students = list(set(self.candidate_id))
        for subject in unique_subjects:
            for student in unique_students:
                index_matched = [i for i in range(len(self.exam_name)) if self.exam_name[i] == subject and self.candidate_id[i]==student]
                index_matched_pass = [i for i in range(len(self.exam_name)) if self.exam_name[i] == subject and self.candidate_id[i]==student and self.grade[i]=='Pass']
                index_matched_fail = [i for i in range(len(self.exam_name)) if self.exam_name[i] == subject and self.candidate_id[i]==student and self.grade[i]=='Fail']
                score_numbers = [int(self.score[i]) for i in range(len(self.exam_name)) if self.exam_name[i] == subject and self.candidate_id[i]==student]

                if score_numbers and max(score_numbers)> self.results[subject][3]:
                    self.results[subject][3] = max(score_numbers)

                if score_numbers and min(score_numbers)< self.results[subject][4]:
                    self.results[subject][4] = min(score_numbers)
                    
                if index_matched:
                    self.results[subject][0] += 1

                if index_matched_pass:
                    self.results[subject][1] += 1

                if index_matched_fail:
                    self.results[subject][2] += 1
        

    def view_result(self):
        print("Exam Name","Number of Candidates","Number of Passed Exams","Number of Failed Exams","Best Score","Worst Score", sep="\t")
        for k,v in self.results.items():
            print(k.ljust(8), ','.ljust(8).join(str(i) for i in v))
        
        

    def create_file(self):
        with open("new_result.csv","w", newline ='') as csvfile:
            writer = csv.writer(csvfile,delimiter = ',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Exam Name","Number of Candidates","Number of Passed Exams","Number of Failed Exams","Best Score","Worst Score"])
            for k,v in self.results.items():
                lst = [k]
                for i in v:
                    lst.append(str(i))
                writer.writerow(lst)
        print("File was created.")
            
            
    
new_report = Report_generator()
new_report.open_file()
new_report.create_table()
new_report.view_result()
new_report.create_file()




        



