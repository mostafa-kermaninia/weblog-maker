from urllib import request, response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post, Comment
from .forms import PostForm
from .serializers import PostSerializer

# نوشته نشدهAPIاين ويوي زير،ساده ترين نوع ويو است و بصورت
''''def index(request):
    return HttpResponse('<h1>welcomeeee</h1>')'''


#  نوشتAPIاما اينبار ميتوان همان ويو را بصورت
# ات قبول كنه را مينويسيAPIريكوئست هايي كه ميخواي HTTPاينجا 
@api_view(['GET' , 'POST'])
def index(request):
    # مياد و داده اي كه ارسال شده رو برميگردونهpostيه ديكشنري خالي برميگردونه ولي براي GETمتود خط پايين،براي ريكوئست هاي
    print(request.data)
    # فقط بايد جيسون بفرستي
    return Response({'message': 'welcomeeee'})
    # حتي ميتوني دايناميك كني پاسخ سرور رو و بگي هر چي كه تو ريكوئست پست برات ميفرستم،همونو برگردون
    # return response(dict(request.data))

def home(request):
    return HttpResponse('<h1>itsssss yourrrrrrr homeeeeee</h1>')


'''
تابع زير،قراره چه كنه؟
  براي كلينت بسازهhtmlقراره يچي تو مايه هاي همون صفحه ي مديريت پست ها كه تو سرور لوكال بهت نشون ميده رو بدون دسترسي مستقيم به ديتابيس و با استفاده از 
'''


# 11111
# اين فقط يك ويوي خالي است


def text_post_list(request):
    # به نوعي رابط بين كد و ديتابيسه و ميتوني باهاش،بري و از تو ديتابيس اطلاعات رو بخونيObjectsاين متود
    posts = Post.objects.all()
    ''' كلينت ميتونه به ليست اسامي و اطلاعات پست ها دسترسي داشته باشه urlsمشخص شده در فايلurlمثلا الان يكاري كردم با دادن
    for post in posts:
        print(post)
        print(post.title)
        print(post.text)
        print(post.is_enable)
        print(post.update_time)
    print(posts) '''

    # هست كه ميتوان نوع آنرا پرينت كردgetنكته: نوع ريكوئستي كه در اين تابع و دوتا تابع پاييني ارسال ميشه به سرور
    print(request.method)  # => "GET"

    return HttpResponse(posts)


# 22222
# وصل ميشوندtemplateهم دارند و به فولدرhtml,css دوتا ويويي كه در اينجا ميسازيم،علاوه بر ويو،كدهاي


def post_list(request):
    posts = Post.objects.all()
    # كه خودمون توش اسم پست هارو ريختيم رو برداره و بفرسته به فايلي كه آدرسشو داديمcontextدستور ميده كه هر بار يه ريكوئست مياد از طرف كلينت،بايد اون ديكشنريrenderاين
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)

# تو اين فايل هر چي ويو ميسازيم در اصل يك فانكشن است،اما ميتوان با كلاس ها هم ويو ساخت
# ميكنهpost_listاين كلاس زير،دقيقا همون كاري رو ميكنه كه تابع


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


def post_details(request, post_id):
    try:
        # اين خط مياد و بين پست هاي ديتابيس ميگرده،اونيكه آيدي اش رو داديم رو برميگردونه
        post = Post.objects.get(pk=post_id)
    # اونوقت همچين اروري هست كه ما ميخوايم هندلش كنيمurlهستن استفاده نكنه و مستقيم يه عدد بزنه توpostsاگر طرف از دكمه هايي كه تو صفحه ي
    except Post.DoesNotExist:
        return HttpResponseNotFound('داداش آيدي درست حسابي بده')
    '''
    اون ارور هندلينگ كه در خط هاي بالا انجام داديم را ميتوان به روش ديگري هم كرد:
        post = get_object_or_404(Post, pk=post_id)
    اينجوري اگر عدد خوبي ندهيم،يك صفحه ي آماده از طرف جنگو نمايان شده و ارور 404 ميدهد
    '''
    # اين خط مياد و تو كامنت هاي ديتابيس ميگرده و اونيكه لينك شده به پستِ مدنظرمون كه تو خط بالايي تعريف كرديم رو برميگردونه
    comments = Comment.objects.filter(post=post)
    # بايد نوشته بشه و استفاده بشهhtmlكليد و مقدار اين ديكشنريه ميتونن متفاوت باشن اما دقت كن كه اونيكه بعنوان استرينگ دادي،تو فايل
    context = {'selected_post': post, 'selected_comments': comments}
    return render(request, 'posts/post_details.html', context=context)

#  رو هم بجاي فانكشنال،با يك كلاس بنويسيمpost_detailsميتوانيم ويوي


class PostDetails(generic.DetailView):
    model = Post
    template_name = 'posts/post_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data()
        # context['selected_post'] = context.pop('post') اگر كدت به مشكل خورد،اين خط رو هم از كامنت در بيار
        context['selected_comments'] = Comment.objects.filter(
            post=kwargs['object'].pk)
        return context

# 33333
# هم داردformدارد و هم يك داده دريافت ميكند پس يك templateاين يكي هم ويو دارد،هم


def post_create(request):
    # نكته:
    # كنيم كه توش فرم هاي خالي موجودنgetدر حين پركردن فرم و ارسال آن،ما اول بايد يه صفحه را
    # استفاده كنيمpost سپس فرم ها را پر كنيم و براي ارسال آنها به ديتابيس و سرور،از
    # پس در اين تابع بايد دو نوع ريكوئست را هندل كنيم

    # 1-POST
    # كار داريم چون قراره اطلاعات رو بفرستيم به سرورPOSTدر اينجا برخلاف توابع قبلي،با ريكوئست هايي از نوع
    if request.method == 'POST':
        # اگر ريكوئست از نوع پست بود،يه فرم در سرور توليد ميشه كه حاوي اطلاعاتيست كه ما وارد كرده ايم
        form = PostForm(request.POST)
        if form.is_valid():
            # اگر داده هاي داخل فرم،مورد تاييد بودن،يعني مثلا بجاي تاريخ عدد نگذاشته بودن،يه فرم نهايي توليد ميشه
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)

            # url دكمه ي سيو رو ميزني،هدايتت ميكنه به اين create post ميدي بهش كه وقتي تو صفحه يurl اينجا يه
            return HttpResponseRedirect('/posts/create')

    # 2-GET
    else:
        # بهش داديم ساخته ميشهformيه فرم خالي با مدلي كه تو فايل
        form = PostForm(request.POST)
        context = {'selected_form': form}

        return render(request, 'posts/post_create.html', context=context)
