from flask import Flask, render_template, url_for, request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
     department_list=['Surgeon','Therapist','Consultant']
     doctors_list=['Mr John','Mr Clark','Ms Chris']
     dropdown_lists=[department_list,doctors_list]

     if request.method=='POST':
        patient_name = request.form.get('inputPatientName')
        doctor_name = request.form.get('inputDoctorName')
        department_name = request.form.get('inputDepartmentName')
        phone = request.form.get('inputPhone')
        symptoms = request.form.get('inputSymptoms')
        date_input = request.form.get('dateInput')
        #return str(patient_name) + str(doctor_name) + str(department_name)+ str(symptoms)+str(phone) +str(date_input)
        success_msg='Your appointment is booked successfully!'
        return render_template('index.html',dropdown_values=dropdown_lists,message=success_msg)
   
     return render_template('index.html',dropdown_values=dropdown_lists,message = '')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/treatment')
def treatment():
    return render_template('treatment.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run()