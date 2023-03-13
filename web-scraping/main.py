# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
from bs4 import BeautifulSoup

url = 'https://www.udemy.com/topic/python/'

print(url);
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Scrape course data
courses = soup.find_all('div', {'class': 'course-card--main--1hHb3'})
for course in courses:
    course_title = course.find('span', {'class': 'course-card--course-title--2f7tE'}).text
    course_rating = course.find('span', {'class': 'udlite-text-xs--text-success--2sLmP'}).text
    course_instructor = course.find('div', {'class': 'course-card--instructor-list--lIA4f'}).text
    print(f'Course: {course_title}\nRating: {course_rating}\nInstructor: {course_instructor}\n')

# Scrape instructor data
instructors = soup.find_all('div', {'class': 'popper--popper-hover--4YJ5J'})
for instructor in instructors:
    instructor_name = instructor.find('div', {'class': 'udlite-heading-md'}).text
    instructor_bio = instructor.find('div', {'class': 'udlite-text-sm'}).text
    instructor_courses = instructor.find('div', {'class': 'udlite-text-xs--course-card--course-list--1Yv_8'}).text
    print(f'Instructor: {instructor_name}\nBio: {instructor_bio}\nCourses: {instructor_courses}\n')