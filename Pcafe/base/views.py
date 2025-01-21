from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import StudentCreationform
from .models import UUIDStudent,StudentData,TranscationHistory,AnalysisTransaction
from django.shortcuts import get_object_or_404
import serial
import time

def getUUID():
    arduino_port = '/dev/ttyACM0'
    baud_rate = 9600
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        print("Starting listening to Arduino")
        time.sleep(2)

        while True:
            if ser.in_waiting > 0:
                rfid_data = ser.readline().decode('utf-8').strip()
                if rfid_data.startswith("UID tag:"):
                    uid = rfid_data.replace("UID tag:", "").strip()
                    print("Scanned RFID UID:", uid)
                    return str(uid)
                else:
                    print("Ignoring data: ", rfid_data)
                    
            time.sleep(0.1)

    except Exception as e:
        print(f"Error reading from serial port: {e}")
        return None

def registerRFID(request):
    context = {}
    if request.method == "POST":
        try:
            rfid_data = getUUID()
            exists_UUID = None
        
            if rfid_data:
                existing_uuid = UUIDStudent.objects.filter(UUID=rfid_data)
                if existing_uuid:
                    print(f"UUID {rfid_data} already exists!")
                    exists_UUID = "UUID Already Exists"
                    context['exist_UUID'] = exists_UUID
                else:
                    new_uuid = UUIDStudent.objects.create(UUID=rfid_data)
                    print(f"New UUID {rfid_data} created with ID {new_uuid.id}")
                    return redirect('Create-Student')
            
                context = {
                    'data': rfid_data
                }
        except Exception as e:
            print(f"Error in Scaning the RFID carc:{e}")
    return render(request, 'registeringRFID.html', context)

def createStudent(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        point = request.POST.get('points')
        uuid = UUIDStudent.objects.last()

        StudentData.objects.create(
            name = name,
            roll = roll,
            phone = phone,
            email = email,
            points = point,
            uuid = uuid,
            profile_picture = uploaded_image
        )
    return render(request,'newStudent.html',context)

def homePage(request):
    context = {}
    temp_variable = None
    if request.method == "POST":
        UUID_data = getUUID()
        try:
            UUID = UUIDStudent.objects.all()
            for i in UUID:
                if(i.UUID==UUID_data):
                    print("Exists in the database")
                    temp_variable = i.UUID
                    return redirect('afterscan',uuid = i.pk)            
        except Exception as e:
            print("Not Found ",e)
    context = {}
    return render(request,"homepage.html",context)

def after_scan_page(request,uuid):
    context = {}
    redirected_uuid = UUIDStudent.objects.get(id = uuid)
    student = get_student_data_by_uuid(redirected_uuid.UUID)
    if request.method == "POST":
        bill = request.POST.get("bill")
        try:
            if(int(bill) < student.points):
                perform_bill_of_student(redirected_uuid.UUID,bill)
                return redirect('homePage')
            else:
                context["Not_Suf"] = "Not sufficient Amount to pay"
        except Exception as e:
            print("Bill not processed",e)
    context = {
        'student':student,
        'uuid':redirected_uuid
    }
    return render(request,'afterscanpage.html',context)


def view_transaction_history(request,uuid):
    context = {}
    try:
        uuid = UUIDStudent.objects.get(id = uuid)
        student = get_student_data_by_uuid(uuid.UUID)
        transactionData = student.transaction_Ofstudent.all()
        context['tr'] = transactionData
   
    except UUIDStudent.DoesNotExist:
        print("the uuid doesnot exists for viewwing transaction")
    return render(request,'TransactionHistory.html',context)

 
def perform_bill_of_student(uuid_data,total_bill):
    try:
        student = get_student_data_by_uuid(uuid_data)
        student.points -= int(total_bill)
        student.save()
        transaction = TranscationHistory.objects.create(
            student = student,
            transcatedPoints = total_bill,
        )
    except student.DoesNotExist:
        print("the student with the uuid doesnot exists")
        
def get_student_data_by_uuid(uuid_data):
    try:
        uuid_from_database = UUIDStudent.objects.get(UUID = uuid_data)
        if uuid_from_database is not None:
            student = uuid_from_database.uuidOFstudent
            return student
    except UUIDStudent.DoesNotExist:
        print("The UUID does not Exist")
        return None
    except student.DoesNotExist:
        print("The student doesnot exists")
        return None
    
def inspect_profile(request):
    context = {}
    if request.method == "POST":
        uuid_data = getUUID()
        student_data = get_student_data_by_uuid(uuid_data)
        if student_data is not None:
            context['Student'] = student_data


    
    return render(request,"inspect_profile.html",context)