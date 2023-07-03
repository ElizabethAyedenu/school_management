# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 00:24:03 2023

@author: LIZZY
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys

from os import path

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"school_design.ui"))

import sqlite3

class Main(QMainWindow, FORM_CLASS):
    selectedBranchId=None
    selectedclassId=None
    selectedemployeeId=None
    selectedstudentId=None
    selectedcourseId=None
    selectedpaymentid=None
    selectedstu_courseId=None
    
    

    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)  
        #GET ALL DATA
        selectedDashBranchItem=0
        self.GET_CLASS_DATA()
        self.GET_BRANCH_DATA()
        self.GET_STUDENT_DATA()
        self.GET_EMPLOYEES_DATA()
        self.GET_COURSES_DATA()
        self.GET_STU_COURSES_DATA()
        self.GET_PAYMENTS_DATA()

        #ASSIGN CLICK EVENTS
        self.add_branch_btn.clicked.connect(self.SAVE_BRANCH_DATA)
        self.add_class_btn.clicked.connect(self.SAVE_CLASS_DATA)
        self.add_employee_btn.clicked.connect(self.SAVE_EMPLOYEE_DATA)
        self.add_student_btn.clicked.connect(self.SAVE_STUDENT_DATA)
        self.course_add_btn.clicked.connect(self.SAVE_COURSES_DATA)
        self.add_payment_btn_3.clicked.connect(self.SAVE_PAYMENTS_DATA)
        self.stu_course_add_btn.clicked.connect(self.SAVE_STU_COURSES_DATA)
        self.Dashboard_branch_drop.currentIndexChanged.connect(self.ListenToDashboardClicked)

        #DELETE CLICK EVENTS
        self.deleteBranchBtn.clicked.connect(self.deleteBranchData)
        self.class_delete_btn.clicked.connect(self.deleteClassData)
        self.employee_delete_btn.clicked.connect(self.deleteEmployeeData)
        self.student_delete_btn.clicked.connect(self.deleteStudentData)
        self.course_delete_btn.clicked.connect(self.deleteCourseData)
        self.delete_payment_btn.clicked.connect(self.deletePaymentData)
        self.stu_course_delete_btn.clicked.connect(self.deleteStu_coursesData)
       
       
       
        #GET TABLE CLICKED
        self.branch_table_widget.cellClicked.connect(self.getBranchClicked)
        self.class_table_widget_2.cellClicked.connect(self.getClassClicked)
        self.employee_table_widget.cellClicked.connect(self.getEmployeeClicked)
        self.student_table_widget.cellClicked.connect(self.getStudentClicked)
        self.course_table_widget.cellClicked.connect(self.getCourseClicked)
        self.payments_table_widget.cellClicked.connect(self.getPaymentClicked)
        self.stu_course_table_widget.cellClicked.connect(self.getStu_coursesClicked)
    
    def ListenToDashboardClicked(self, data):
        global selectedDashBranchItem
        selectedDashBranchItem=self.Dashboard_branch_drop.currentData()
        self.GET_STUDENT_DATA()
        self.GET_EMPLOYEES_DATA()
        self.GET_PAYMENTS_DATA()

        

    
        

    
    def getBranchClicked(self, row, column):
        global selectedBranchId
        print(self.branch_table_widget.item(row, 0 ).text())

        selectedBranchId=self.branch_table_widget.item(row, 0 ).text()
        self.add_branch_btn.setText("Update Branch")

        #self.branch_selected_id.setText( self.branch_table_widget.item(row, 0 ).text() )
        self.branch_name.setText( self.branch_table_widget.item(row, 1 ).text() )
       # self.branch_type_drop.itemText( self.branch_table_widget.item(row, 2 ).text() )
        self.branch_location.setText( self.branch_table_widget.item(row, 3 ).text() )


    def deleteBranchData(self):
        global selectedBranchId
        print( selectedBranchId) 
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  branches where branch_id=(?)",(selectedBranchId) )
        db.commit()
        cursor.close()
        self.GET_BRANCH_DATA()

    def getClassClicked(self, row, column):
        global selectedclassId
        print(self.class_table_widget_2.item(row, 0 ).text())
        selectedclassId=self.class_table_widget_2.item(row, 0 ).text() 
        # self.class_branch_type_drop.setText( self.class_table_widget_2.item(row, 1 ).text() )
        self.class_name.setText( self.class_table_widget_2.item(row, 2 ).text() )
        self.add_class_btn.setText("Update Class")



    def deleteClassData(self):
        global selectedclassId
        print(selectedclassId)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  classes where class_id=(?)",(selectedclassId))
        db.commit()
        cursor.close()
        self.GET_CLASS_DATA() 


    def getEmployeeClicked(self, row, column):
        global selectedemployeeId
        print(self.employee_table_widget.item(row, 0 ).text())
        selectedemployeeId=self.employee_table_widget.item(row, 0 ).text() 
        self.Employee_name_3.setText( self.employee_table_widget.item(row, 1 ).text() )
        self.Employee_Phone_btn.setText( self.employee_table_widget.item(row, 3 ).text() )
        self.Employee_Address_btn_2.setText( self.employee_table_widget.item(row, 4).text() )
        self.Employee_Email_btn.setText( self.employee_table_widget.item(row, 5 ).text() )
        self.add_employee_btn.setText("Update Employee")


    def deleteEmployeeData(self):
        global selectedemployeeId
        print(selectedemployeeId)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  employees where employee_id=(?)",(selectedemployeeId))
        db.commit()
        cursor.close()
        self.GET_EMPLOYEES_DATA()  

    def getStudentClicked(self, row, column):
        global selectedstudentId
        print(self.student_table_widget.item(row, 0 ).text())
        selectedstudentId= self.student_table_widget.item(row, 0 ).text() 
        self.Student_name_btn.setText( self.student_table_widget.item(row, 1 ).text() )
        self.Student_name_btn_2.setText( self.student_table_widget.item(row, 2 ).text() )
        self.add_student_btn.setText("Update Student")

    def deleteStudentData(self):
        global selectedstudentId
        print(selectedstudentId)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  students where student_id=(?)",(selectedstudentId))
        db.commit()
        cursor.close()
        self.GET_STUDENT_DATA()  
 
    
    def getCourseClicked(self, row, column):
        global selectedcourseId
        print(self.course_table_widget.item(row, 0 ).text())
        selectedcourseId= self.course_table_widget.item(row, 0 ).text() 
        self.Course_name_btn.setText( self.course_table_widget.item(row, 1 ).text() )
        self.Course_price_btn.setText( self.course_table_widget.item(row, 2 ).text() )
        self.course_add_btn.setText("Update Course")
       

    def deleteCourseData(self):
        global selectedcourseId
        print(selectedcourseId)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  courses where course_id=(?)",(selectedcourseId))
        db.commit()
        cursor.close()
        self.GET_COURSES_DATA()  


    def getPaymentClicked(self, row, column):
        global selectedpaymentid
        print(self.payments_table_widget.item(row, 0 ).text())
        selectedpaymentid= self.payments_table_widget.item(row, 0 ).text() 
        # newFormat=QtCore.QDateTime.fromString(self.payments_table_widget.item(row, 4 ).text(), "dd/mm/yyyy")
        # self.payment_date_edit.setDate(newFormat)
        self.Payment_amount.setText(self.payments_table_widget.item(row, 6 ).text() )
        self.add_payment_btn_3.setText("Update Payment")
        

    def deletePaymentData(self):
        global selectedpaymentid
        print(selectedpaymentid)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  payments where payment_id=(?)",(selectedpaymentid))
        db.commit()
        cursor.close()
        self.GET_PAYMENTS_DATA()  
 
    def getStu_coursesClicked(self, row, column):
        global selectedstu_courseId
        print(self.stu_course_table_widget.item(row, 0 ).text())
        selectedstu_courseId=self.stu_course_table_widget.item(row, 0 ).text()
        self.stu_course_add_btn.setText("Update Student Course")
       

    def deleteStu_coursesData(self):
        global selectedstu_courseId
        print(selectedstu_courseId)
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        cursor.execute("delete from  students_courses where student_course_id=(?)",(selectedstu_courseId))
        db.commit()
        cursor.close()
        self.GET_STU_COURSES_DATA() 
 

    def insert_values(self,sqlCommand):
         db=sqlite3.connect("school.db")
         cursor=db.cursor()
         cursor.execute(sqlCommand) 
         db.commit()
         cursor.close()
        
  
    #MAIN METHJOD TO LOAD DATA FROM DATABASE
    def GET_DATA_FROM_DB(self, sqlCommand):
        #connect to Sqlite3 database and fill GUI table with data.
       db=sqlite3.connect("school.db")
       cursor=db.cursor()
       return cursor.execute(sqlCommand)
        
   
    
    def GET_BRANCH_DATA(self): 
        global selectedBranchId
        query=''' SELECT * from Branches ''' 
        self.branch_table_widget.setRowCount(0)
        self.add_branch_btn.setText("Add Branch")
        selectedBranchId=None
        totalBranch=0
        
        
        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            totalBranch=totalBranch+1
            self.branch_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.branch_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.Total_branch_label.setText(str(totalBranch))
        for item_data in self.GET_DATA_FROM_DB(query):
            self.Employee_branch_drop.addItem(item_data[1],item_data[0],  )
            self.class_branch_type_drop.addItem(item_data[1], item_data[0])
            self.student_branch_drop.addItem(item_data[1], item_data[0])
            self.payment_branch_drop.addItem(item_data[1], item_data[0])
            self.course_branch_drop.addItem(item_data[1], item_data[0]) 
            self.Dashboard_branch_drop.addItem(item_data[1], item_data[0]) 
            
  
        
    def GET_CLASS_DATA(self): 
        global selectedclassId
        query=''' SELECT * from classes ''' 
        self.class_table_widget_2.setRowCount(0)
        self.add_class_btn.setText("Add Branch")
        selectedclassId=None
        
        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            self.class_table_widget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.class_table_widget_2.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        for item_data in self.GET_DATA_FROM_DB(query):
            self.student_class_drop.addItem(item_data[2], item_data[0])
        
    # here is our code
    
    
    def GET_STUDENT_DATA(self): 
        global selectedDashBranchItem
        global selectedstudentId
        query=''' SELECT * from students ''' 
        self.student_table_widget.setRowCount(0)
        selectedstudentId= None
        totalStudents=0
        totaldashStudents=0

        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            
            totalStudents=totalStudents+1
            if(selectedDashBranchItem==row_data[3]):
                totaldashStudents=totaldashStudents+1
        
            self.student_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.student_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.Total_students_label.setText(str(totalStudents))
        self.Branch_student_label.setText(str(totaldashStudents))
        for item_data in self.GET_DATA_FROM_DB(query):
            self.payment_student_drop.addItem(item_data[1],item_data[0])
            self.stu_course_student_drop_btn.addItem(item_data[1],item_data[0])
            
    # here is our code
    
    def GET_EMPLOYEES_DATA(self): 
        global selectedDashBranchItem
        global selectedemployeeId

        query=''' SELECT * from employees ''' 
        
        self.employee_table_widget.setRowCount(0)
        selectedemployeeId=None
        totalEmp=0
        totalTeacher=0
        # total number of employee and teacher by branch
        totalDashEmp=0
        totalDashteacher=0
                
        
        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            totalEmp=totalEmp+1
            if(row_data[2]=="Teacher"):
                totalTeacher=totalTeacher+1
                

            if(selectedDashBranchItem==row_data[6]):
                totalDashEmp=totalDashEmp+1
            
            if(selectedDashBranchItem==row_data[6]) & (row_data[2]=="Teacher"):
                totalDashteacher=totalDashteacher+1


            self.employee_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.employee_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        self.branch_employee_label.setText(str(totalDashEmp))
        self.Branch_teacher_label.setText(str(totalDashteacher))
        self.Total_employee_label.setText(str(totalEmp))
        self.Total_teachers_label.setText(str(totalTeacher))
        for item_data in self.GET_DATA_FROM_DB(query):
            self.course_employee_drop.addItem(item_data[1],item_data[0])
    # here is our code
    
    def GET_COURSES_DATA(self): 
        global selectedcourseId
        query=''' SELECT * from courses ''' 
        
        self.course_table_widget.setRowCount(0)
        selectedcourseId=None
        
        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            self.course_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.course_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        for item_data in self.GET_DATA_FROM_DB(query):
            self.payment_course_drop.addItem(item_data[1],item_data[0])
            self.stu_course_course_drop.addItem(item_data[1],item_data[0])
            
    # here is our code
    
    def GET_PAYMENTS_DATA(self):
        global selectedDashBranchItem
        global selectedpaymentid        
        query=''' SELECT * from payments '''        
        self.payments_table_widget.setRowCount(0)
        selectedpaymentid=None 
        totalRevenue=0
        # Total Revenue by branch
        totalBranchRevenue=0     

        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            totalRevenue=totalRevenue+row_data[6]

            if(selectedDashBranchItem==row_data[2]) :
                totalBranchRevenue=totalBranchRevenue+ row_data[6]

            self.payments_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.payments_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
            self.Total_revenue_label.setText(str(totalRevenue))
            self.Branch_revenue_label.setText(str(totalBranchRevenue))
                
    # here is our code
    
    def GET_STU_COURSES_DATA(self):
        global selectedstu_courseId
        query=''' SELECT * from students_courses ''' 
        
        self.stu_course_table_widget.setRowCount(0)
        selectedstu_courseId=None
        
        for row_number, row_data in enumerate(self.GET_DATA_FROM_DB(query)):
            self.stu_course_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.stu_course_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(data)))    
    # here is our code
    
    
    def SAVE_BRANCH_DATA(self):
        global selectedBranchId
        br_name=self.branch_name.text()
        br_type=self.branch_type_drop.currentText()
        br_address=self.branch_location.text()
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedBranchId==None):
            cursor.execute("INSERT INTO branches(name,type,address) VALUES(?,?,?)",(br_name, br_type, br_address) )
        else:
             cursor.execute("update branches set name=(?),type=(?),address(?) where branch_id=(?)",(br_name, br_type, br_address, selectedBranchId) )
        db.commit()
        cursor.close()
        self.GET_BRANCH_DATA()

    def SAVE_CLASS_DATA(self):
        global selectedclassId
        cl_name=self.class_name.text()
        cl_branch_id=str(self.class_branch_type_drop.currentData())
        
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedclassId==None):
            cursor.execute("INSERT INTO classes(name,branch_id) VALUES(?,?)",(cl_name, cl_branch_id) )
        else:
             cursor.execute("update classes set name=(?), branch_id=(?) where class_id=(?)",(cl_name, cl_branch_id,selectedclassId) )
        db.commit()
        cursor.close()
        self.GET_CLASS_DATA()

    def SAVE_EMPLOYEE_DATA(self):
        global selectedemployeeId
        emp_name=self.Employee_name_3.text()
        emp_type=self.Employee_type_drop_3.currentText()
        emp_phone=self.Employee_Phone_btn.text()
        emp_address=self.Employee_Address_btn_2.text()
        emp_email=self.Employee_Email_btn.text()
        emp_branch_id=str(self.Employee_branch_drop.currentData())
        
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedemployeeId==None):
            cursor.execute("INSERT INTO employees(name,type,phone_number,address,email_address,branch_id) VALUES(?,?,?,?,?,?)",(emp_name,emp_type,emp_phone,emp_address,emp_email,emp_branch_id) )
        else:
             cursor.execute("update employees set name=(?),type=(?),phone_number=(?),address=(?),email_address=(?),branch_id=(?) where employee_id=(?)",(emp_name,emp_type,emp_phone,emp_address,emp_email,emp_branch_id,selectedemployeeId) )
        db.commit()
        cursor.close()
        self.GET_EMPLOYEES_DATA()

    def SAVE_STUDENT_DATA(self):
        global selectedstudentId
        stu_name=self.Student_name_btn.text()
        stu_phone=self.Student_name_btn_2.text()
        stu_branch_id=str(self.student_branch_drop.currentData())
        stu_class_id=str(self.student_class_drop.currentData())
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedstudentId==None):
            cursor.execute("INSERT INTO students(name,phone_number,branch_id,class_id) VALUES(?,?,?,?)",(stu_name,stu_phone,stu_branch_id,stu_class_id) )
        else:
            cursor.execute("update students set name=(?),phone_number=(?),branch_id=(?),class_id=(?) where student_id=(?)",(stu_name,stu_phone,stu_branch_id,stu_class_id,selectedstudentId) )
        db.commit()
        cursor.close()
        self.GET_STUDENT_DATA()

    def SAVE_COURSES_DATA(self):
        global selectedcourseId
        course_price=self.Course_price_btn.text()
        course_name=self.Course_name_btn.text()
        course_branch_id=str(self.course_branch_drop.currentData())
        course_emp_id=str(self.course_employee_drop.currentData())
                
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedcourseId==None):
            cursor.execute("INSERT INTO courses(price,name,branch_id,employee_id) VALUES(?,?,?,?)",(course_price,course_name,course_branch_id,course_emp_id) )
        else:
            cursor.execute("update courses set price=(?),name=(?),branch_id=(?),employee_id=(?) where course_id=(?)",(course_price,course_name,course_branch_id,course_emp_id,selectedcourseId) )
        db.commit()
        cursor.close()
        self.GET_COURSES_DATA()

    def SAVE_PAYMENTS_DATA(self):
        global selectedpaymentid
        pay_stu_id=str(self.payment_student_drop.currentData())
        pay_branch_id=str(self.payment_branch_drop.currentData())
        pay_course_id=str(self.payment_course_drop.currentData())
        pay_payment_type=self.payment_type_drop.currentText()
        pay_date=self.payment_date_edit.text()
        pay_amount=self.Payment_amount.text()
                
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if (selectedpaymentid==None):
            cursor.execute("INSERT INTO payments(student_id,branch_id,course_id,payment_type,date,amount) VALUES(?,?,?,?,?,?)",(pay_stu_id,pay_branch_id,pay_course_id,pay_payment_type,pay_date,pay_amount) )
        else :
            cursor.execute("update payments set student_id=(?),branch_id=(?),course_id=(?),payment_type=(?),date=(?),amount=(?) where payment_id=(?)",(pay_stu_id,pay_branch_id,pay_course_id,pay_payment_type,pay_date,pay_amount,selectedpaymentid))
        db.commit()
        cursor.close()
        self.GET_PAYMENTS_DATA()
    
    def SAVE_STU_COURSES_DATA(self):
        global selectedstu_courseId
        stu_course_student_id=str(self.stu_course_student_drop_btn.currentData())
        stu_course_course_id=str(self.stu_course_course_drop.currentData())
        db=sqlite3.connect("school.db")
        cursor=db.cursor()
        if(selectedstu_courseId==None):
            cursor.execute("INSERT INTO students_courses(student_id,course_id) VALUES(?,?)",(stu_course_student_id,stu_course_course_id) )
        else:
            cursor.execute("update students_courses set student_id=(?),course_id=(?) where student_course_id=(?)",(stu_course_student_id,stu_course_course_id,selectedstu_courseId))
        db.commit()
        cursor.close()
        self.GET_STU_COURSES_DATA()
    
def main():
    global selectedDashBranchItem
    selectedDashBranchItem=0

    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
    
if __name__=='__main__':
    main()