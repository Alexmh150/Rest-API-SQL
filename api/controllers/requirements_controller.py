from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine, func, text
from sqlalchemy.orm import sessionmaker

# Create Blueprint to be modular
requirements_bp = Blueprint('requirements_bp', __name__)

# Create connection with database
database_name = 'sqlite:///database.db'
engine = create_engine(database_name)
Session = sessionmaker(bind=engine)

# Declare route for api
@requirements_bp.route('/jobs', methods=['GET'])
def get_job_details():

    # Get parameters from api
    year = int(request.args.get('year',2021))
    
    try:
        session = Session()

        # Declare sql statement directly
        query = text(f"""with quarters as 
                        (
                            select e.id, 
                                CASE
                                    WHEN strftime('%m', e.[datetime]) BETWEEN '01' AND '03' THEN 'Q1'
                                    WHEN strftime('%m', e.[datetime]) BETWEEN '04' AND '06' THEN 'Q2'
                                    WHEN strftime('%m', e.[datetime]) BETWEEN '07' AND '09' THEN 'Q3'
                                    WHEN strftime('%m', e.[datetime]) BETWEEN '10' AND '12' THEN 'Q4'
                                END AS quarter,
                                j.job,
                                d.department
                                from Employee e
                            inner join DimJob j on e.job_id = j.id 
                            inner join DimDepartment d on e.department_id = d.id 
                            where strftime('%Y', e.[datetime]) = '2021'
                        )
                        select department, job,
                            count(1) filter (where quarter = 'Q1') as q1,
                            count(1) filter (where quarter = 'Q2') as q2,
                            count(1) filter (where quarter = 'Q3') as q3,
                            count(1) filter (where quarter = 'Q4') as q4 
                        from quarters
                        group by department, job
                        order by department, job
                                     """)
        
        # Retrieve the data
        with engine.connect() as connection:
            results = connection.execute(query).all()

        # Build response
        departments = []
        for result in results:
            department = {
                "department":result.department,
                "job":result.job,
                "q1":result.q1,
                "q2":result.q2,
                "q3":result.q3,
                "q4":result.q4
            }
            departments.append(department)
        
        session.close()

        return jsonify(departments), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@requirements_bp.route('/departments', methods=['GET'])
def get_department_details():
    
    year = int(request.args.get('year',2021))
    
    try:
        session = Session()

        # Declare sql statement directly
        query = text(f"""with employees_by_department as 
                        (
                            select department_id, count(id) as num_employees 
                            from employee 
                            where department_id is not null
                            group by department_id
                        )
                        select d.id, d.department, count(e.id) as hired from Employee e
                        inner join DimDepartment d on e.department_id = d.id
                        group by d.id, d.department
                        having count(e.id) > (select avg(num_employees) as avg_num_employees from employees_by_department)
                        order by count(e.id) desc
                                                            """)
                                
        # Retrieve the data
        with engine.connect() as connection:
            results = connection.execute(query).all()

        # Build response
        departments = []
        for result in results:
            department = {
                "id":result.id,
                "department":result.department,
                "hired":result.hired,
            }
            departments.append(department)
        
        session.close()

        return jsonify(departments), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400