import streamlit as st
from course import Course
from teacher import Teacher
from customer import Customer
from web_management import Web_Management

def main():
    st.title("Online Education store")

    choice = st.radio("Are you teacher/ customer", ("teacher", "Customer"))
     if choice == "Teacher":
         st.subheader("teacher portal")
         teacher_id = st.text_input("Enter your Id :")
         teacher_name = st.text_input("enter your name :")

         teacher = Teacher(teacher_id, teacher_name)

         Web_Management.add_teacher(teacher)

         if st.button("create course"):
            course_id = st.text_input("Enter course_Id")
            course_name = st.text_input("Enter course_Name :")
            course_description = st.number_input("enter description")
            course_price = st.text_input("Enter price :")
            course_duration = st.text_input("enter course duration")
            course_instructor = st.text_input("Enter instructor name :")

            course = Course(course_id, course_name, course_price, course_description, course_duration, course_instructor)
     Web_Management.add_course(course)
     st.success("course Added Successfuly!!")

    elif choice == "customer":
        st.subheader("Customer portal")
        customer_id = st.text_input("Enter customer id :")
        customer_name = st.text_input("Enter the customer name :")

        customer = Customer(customer_id, customer_name)

    Web_Management.add_customer(customer)

        if st.button("show All course"):
            available_course = web_management.display_available_courses()

           if not available_course:
               st.write("no course available")

           else:
