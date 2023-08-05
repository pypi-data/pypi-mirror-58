=========
thStorage
=========

thStorage is a simple app to connect to th clusters' storage system

detail documentation is in the "docs" directory

Quick start

-----------

1. Install based pubgins [django restframework;requests] like this::

   'pip install djangorestframework==3.11.0'
   'pip install requests'

2. Add "rest_framework" and "thStorage" to your INSTALLED_APPS setting like this::

    INSTALL_APPS = [
        ...
        'thStorage',
        'rest_framework',
    ]

3. Include the thStorage URLconf in your project urls.py like this::

    from thStorage import urls as thStorageUrls
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('login/', main.login),
    ] + thStorageUrls.urlpatterns

4. Run `python manage.py migrate` to create thStorage models

5. Run `python manage.py collectstatic` to migrate thStorage statics

6. Set django project settings like::

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        )
    } # restful api csrftoken!!!!!!

    X_FRAME_OPTIONS = 'ALLOWALL' # (or your host name)
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR,"static").replace("\\","/")
    TH_STORAGE_CONFIG = {
        'TOKEN_UPDATE_IMTERVAL': 36000000,
        'STORAGE_BACKEND_HOST':'thstorage backend server',
        'STORAGE_BACKEND_APPID':'your thstorage appid',
        'STORAGE_BACKEND_APPKEY':'your thstorage appkey',
    }

7. Login thstorage when your project's user login like this::

    from thStorage.models import THStorageUser
    ...
    systemUsername = user.username  # systemUsername is tianhe system (in nscc-tj) username, and username is your project username
    cluster = "TH-HPC1" # cluster is tianhe system cluster name
    thStorageUser = THStorageUser(username,cluster,systemUsername)
    thStorageUser.Login()

8. Set LocalStorage in login redirect page like this::

    from thStorage.thstorage import THStorageUser
    ...
    username = request.user.username
    systemUsername = request.session.get("systemUsername","")
    cluster = request.session.get("cluster","")
    thStorageUser = THStorageUser(username, cluster, systemUsername)
    t, u, c, s = thStorageUser.Login()
    thst = {"token": t, "username": s, "cluster": c,"platform":"default"}
    return render(request, 'index.html', {"thst":thst})

    edit index.html
    <script>
        var platform = "{{thst.platform}}";
        var username = "{{thst.username}}";
        var cluster = "{{thst.cluster}}";
        var token = "{{thst.token}}";
        localStorage.setItem("platform", platform);
        localStorage.setItem("username", username);
        localStorage.setItem("cluster", cluster);
        localStorage.setItem("token", token);
    </script>

9. Add url "/thStorage" to your storage page by iframe::

    <body>
        <div> your html elements </div>
        <div>
            <iframe id="myiframe" src="/thstorage" frameborder="0" width="100%" height="100%"></iframe>
        </div>
    </body>
    <script>
        var ifm= document.getElementById("myiframe"); //or set as your div element's height
        ifm.height=document.documentElement.clientHeight;
    </script>

10. Add thStorage's NetDiskUser to admin::

    from thStorage.models import NetDiskUser
    # Register your models here.
    admin.site.register(NetDiskUser)

11. Test thStorage::
    Run `python manage.py createsuperuser`
    add a admin user
    add a test user to thStorage's NetDiskUser by admin (user must map to real th systemuser)

12. Start the development server and visit http://127.0.0.1:8000/yourLoginUrl then login and enjoy it!