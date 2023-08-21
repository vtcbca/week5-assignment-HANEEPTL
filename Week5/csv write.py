import csv
f=open('c:\\sqlite3\\csv\\student.csv','w',newline='')
w=csv.writer(f)
header=["id","name","city","contact"]
w.writerow(header)
row=[[1,"hanee","bardoli",8976567569],[2,"heer","tarsadi",6574321678],[3,"riya","surat",8796754678],[4,"krisha","baroda",8796543215]]
w.writerows(row)
f.close()
