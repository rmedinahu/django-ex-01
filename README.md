# django-ex-01 - Sample Django Application for Matching Recruits with Jobs

## Nov 19 - OOP - Override Generics - Composition

### Clone or (re)fork this repository to your development machine.

#### Once cloned ... 

1. activate (or create) the virtual environment (python3 required)

2. CD to project root

3. Run:

```pip install -r requirements.txt```

```python manage.py migrate```

```python manage.py createsuperuser``` (provide info when prompted)

```python manage.py runserver```

4. Add a link to the menu bar that connects to the admin. Modify ```base.html``` with ```{% url '' %}``` template function.

5. Add some recruits, jobs, and recruit/job associations using the admin.

6. In ```RecruitView```, sort the job list by preference ascending.



