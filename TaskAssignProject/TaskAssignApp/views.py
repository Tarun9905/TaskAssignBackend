# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from .serializers import UserSerializer, TaskSerializer
# from .models import User, Task
# from django.views import View
# from django.utils.decorators import method_decorator
# from django.db import IntegrityError
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserRegister(View):
#     def post(self, request):
#         data = JSONParser().parse(request)
#         userserializer = UserSerializer(data=data)
#         if userserializer.is_valid():
#             try:
#                 userserializer.save()
#                 return JsonResponse({'message': 'User Registration Completed'}, status=200)
#             except IntegrityError:
#                 return JsonResponse({'error': 'Email already registered'}, status=400)
#         return JsonResponse(userserializer.errors, status=400)
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserLogin(View):
#     def post(self, request):
#         data = JSONParser().parse(request)
#         email = data.get('email')
#         password = data.get('password')
#
#         try:
#             user = User.objects.get(email=email)
#             if user.password == password:
#                 return JsonResponse({
#                     'message': 'Login successful',
#                     'user': {
#                         'name': user.name,
#                         'email': user.email,
#                         'phone': user.phone
#                     }
#                 }, status=201)
#             else:
#                 return JsonResponse({'error': 'Incorrect password'}, status=401)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=404)
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserList(View):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False, status=200)
#
# @method_decorator(csrf_exempt, name='dispatch')
# class TaskView(View):
#     def get(self, request):
#         """Fetch all tasks"""
#         tasks = Task.objects.all()
#         task_serializer = TaskSerializer(tasks, many=True)
#         return JsonResponse(task_serializer.data, safe=False, status=200)
#
#     def post(self, request):
#         try:
#             data = JSONParser().parse(request)
#             serializer = TaskSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'message': 'Task added successfully'}, status=201)
#             return JsonResponse(serializer.errors, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#
#     def put(self, request, id):
#         """Update assigned user of a task"""
#         try:
#             data = JSONParser().parse(request)
#             assigned_user = data.get("assigned_user")
#
#             if not assigned_user:
#                 return JsonResponse({'error': 'Assigned user is required'}, status=400)
#
#             try:
#                 task = Task.objects.get(id=id)
#                 task.assigned_user = assigned_user
#                 task.save()
#                 return JsonResponse({'message': 'Task updated successfully'}, status=200)
#             except Task.DoesNotExist:
#                 return JsonResponse({'error': 'Task not found'}, status=404)
#
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#
#     def delete(self, request, id):
#         """Delete a task by ID"""
#         try:
#             task = Task.objects.get(id=id)
#             task.delete()
#             return JsonResponse({"message": "Task deleted successfully!"}, status=204)
#         except Task.DoesNotExist:
#             return JsonResponse({"error": "Task not found"}, status=404)
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UpdateTaskStatusView(View):
#     def put(self, request, id):
#         """Update task status after verifying email and password"""
#         try:
#             data = JSONParser().parse(request)
#             email = data.get("email")
#             password = data.get("password")
#             new_status = data.get("status")
#
#             try:
#                 user = User.objects.get(email=email)
#                 if user.password != password:
#                     return JsonResponse({'error': 'Invalid password'}, status=401)
#             except User.DoesNotExist:
#                 return JsonResponse({'error': 'User not found'}, status=404)
#
#             try:
#                 task = Task.objects.get(id=id)
#                 task.status = new_status
#                 task.save()
#                 return JsonResponse({'message': 'Task status updated successfully'}, status=200)
#             except Task.DoesNotExist:
#                 return JsonResponse({'error': 'Task not found'}, status=404)
#
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class TaskByUserNameView(View):
#     def get(self, request, name):
#         """Return only tasks assigned to a specific user by name"""
#         try:
#             tasks = Task.objects.filter(assigned_user__iexact=name)
#             serializer = TaskSerializer(tasks, many=True)
#             return JsonResponse(serializer.data, safe=False, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task
from django.views import View
from django.utils.decorators import method_decorator
from django.db import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class UserRegister(View):
    def post(self, request):
        data = JSONParser().parse(request)
        userserializer = UserSerializer(data=data)
        if userserializer.is_valid():
            try:
                userserializer.save()
                return JsonResponse({'message': 'User Registration Completed'}, status=200)
            except IntegrityError:
                return JsonResponse({'error': 'Email already registered'}, status=400)
        return JsonResponse(userserializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UserLogin(View):
    def post(self, request):
        data = JSONParser().parse(request)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return JsonResponse({
                    'message': 'Login successful',
                    'user': {
                        'name': user.name,
                        'email': user.email,
                        'phone': user.phone
                    }
                }, status=201)
            else:
                return JsonResponse({'error': 'Incorrect password'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class UserList(View):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def get(self, request):
        """Fetch tasks with optional filtering for priority and status"""
        try:
            priority_filter = request.GET.get('priority')  # 'high-low' or 'low-high'
            status_filter = request.GET.get('status')      # 'todo', 'inprogress', 'complete'

            tasks = Task.objects.all()

            if status_filter:
                tasks = tasks.filter(status__iexact=status_filter)

            if priority_filter == 'high-low':
                tasks = tasks.order_by('-priority')
            elif priority_filter == 'low-high':
                tasks = tasks.order_by('priority')

            task_serializer = TaskSerializer(tasks, many=True)
            return JsonResponse(task_serializer.data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Task added successfully'}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, id):
        """Update assigned user of a task"""
        try:
            data = JSONParser().parse(request)
            assigned_user = data.get("assigned_user")

            if not assigned_user:
                return JsonResponse({'error': 'Assigned user is required'}, status=400)

            try:
                task = Task.objects.get(id=id)
                task.assigned_user = assigned_user
                task.save()
                return JsonResponse({'message': 'Task updated successfully'}, status=200)
            except Task.DoesNotExist:
                return JsonResponse({'error': 'Task not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return JsonResponse({"message": "Task deleted successfully!"}, status=204)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateTaskStatusView(View):
    def put(self, request, id):
        try:
            data = JSONParser().parse(request)
            email = data.get("email")
            password = data.get("password")
            new_status = data.get("status")

            try:
                user = User.objects.get(email=email)
                if user.password != password:
                    return JsonResponse({'error': 'Invalid password'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

            try:
                task = Task.objects.get(id=id)
                task.status = new_status
                task.save()
                return JsonResponse({'message': 'Task status updated successfully'}, status=200)
            except Task.DoesNotExist:
                return JsonResponse({'error': 'Task not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class TaskByUserNameView(View):
    def get(self, request, name):
        try:
            tasks = Task.objects.filter(assigned_user__iexact=name)
            serializer = TaskSerializer(tasks, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
