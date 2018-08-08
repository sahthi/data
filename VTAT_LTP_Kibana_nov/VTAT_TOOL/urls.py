from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import django.contrib.auth.views
from django.contrib.auth.views import logout
from VTAT_TOOL.views import index,create_repository,add_repository,view_repository,execute_repository,show_script_logs
from VTAT_TOOL.views import run_repository,monitor_execution,file_not_found_error,results_repository,DeviceBranchList,delete_repository
from VTAT_TOOL.views import show_monitor_script_logs,modify_repository,monitor_clear_records
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^accounts/login/$', django.contrib.auth.views.login,name='login'),
    url(r'^$',index, name='index'),
    url(r'^createRepository/$',create_repository, name='create_repository'),
    url(r'^addRepository/$',add_repository, name='add_repository'),
    url(r'^viewRepository/$',view_repository, name='view_repository'),
    #url(r'^modifyRepository/$',modify_repository, name='view_repository'),
    url(r'^deleteRepository/$',delete_repository, name='execute_repository'),
    url(r'^executeRepository/$',execute_repository, name='execute_repository'),
    url(r'^runPlanExecution/$',run_repository, name='run_repository'),
    url(r'^resultRepository/$',results_repository, name='results_repository'),
    url(r'^monitorExecution/$',monitor_execution, name='monitor_execution'),
    url(r'^modifyRepository/$',modify_repository, name='modify_repository'),
    url(r'^showScriptLog/$',show_script_logs, name='show_script_logs'),
    url(r'^monitorScriptLogs/$',show_monitor_script_logs, name='show_script_result'),
    url(r'^clearRecords/$',monitor_clear_records, name='monitor_clear_records'),
    url(r'^NotFound/$',file_not_found_error, name='error'),
    url(r'^logout/$', django.contrib.auth.views.logout,{'next_page': '/accounts/login/'},name="logout"),
    url(r'^test/$',DeviceBranchList, name='test'),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

