import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'ak'
    password = '123454321'
    grading_system.login(username,password)

def test_check_password(grading_system):
    username = 'akend3'
    password =  2
    grading_system.usr.check_password(username,password)

def test_TA_change_grade(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.change_grade('yted91','software_engineering', 'assignment1',0)
    grading_system.reload_data()

def test_TA_create_assignment(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.create_assignment('testing','4/3/2022','comp_sci')
    grading_system.reload_data()

def test_prof_add_student(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.add_student('yted91', 'databases')
    grading_system.reload_data()

def test_prof_drop_student(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.drop_student('hdjsr7', 'databases')
    grading_system.reload_data()

def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')
    grading_system.reload_data()

def test_check_ontime(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.check_ontime('2/3/2020','2/3/2020')
    grading_system.reload_data()

def test_check_grades(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.check_grades('cloud_computing')
    grading_system.reload_data()

def test_view_assignments(grading_system):
     grading_system.login('akend3', '123454321')
     grading_system.usr.view_assignments('cloud_computing')
     grading_system.reload_data()

def test_TA_check_grades(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.check_grades('hdjsr7','cloud-computing')

def test_prof_check_grades(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.check_grades('tvmfp8','cloud-computing')

def test_prof_create_assignment(grading_system):
    grading_system.login('saab','bestTA')
    grading_system.usr.create_assignment('testing','4/3/2022','comp_sci')
    grading_system.reload_data()

def test_prof_check_ontime(grading_system):
    grading_system.login('goggins','augurrox')
    grading_system.usr.check_ontime('04-03-2022','04-03-2022')
    grading_system.reload_data()

def test_TA_submit_assignment(grading_system):
    grading_system.login('cmhbf5','bestTA')
    grading_system.usr.submit_assignment('cloud_computing','assignment1','blahhhh','4-3-2022')
    grading_system.reload_data()


    


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem