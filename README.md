# Ques10

Date | Learned | Task Completed
-----|---------|----------------
10-27 March | Celery ,Celery-beat, django-celery-beat, django-celery-results, django-debugging-toolbar, rabbit-mq, kwargs, args, static method, git commands. | Introduce Levels and restrictions associated with it, update user level based on score using celery.
28-29 March |  Holi   | Holi
30-31 March | Signals : (Post_save) , bulk_create , mysql -u username -p, transaction atomic, bulk_update,[filter() Python ](https://www.programiz.com/python-programming/methods/built-in/filter) | Explain how message is sent on following a post (Folllow Button)
1-3 April|Signals : [pre_save](https://medium.com/@singhgautam7/django-signals-master-pre-save-and-post-save-422889b2839), [SELECT,ORDER BY,WHERE,DESC](https://www.mysqltutorial.org/), custom tags (register.filter, inclusion_tag, simple_tag)  |Customize messages UI, Filter messages by user, Messages on level update
4-8 April | ajax, too many edge cases | Follow bell icon (a Vote type) and Subscription
9-14 April | Merge Tags Functionality --> Admin Panel Customization : Custom Filter, Custom Actions, AdminForm(Prefill) + Sessions, ModelManager, add and remove objects without altering main model (tags.add(), tags.remove), url canocolization, slugs importance, Mysql DROP and CREATE DB, makemigrations vs migrate. | Merge Tags Functionality (Parent - Children method)
15-24 April | db_index=True(WHERE), URLs designing importance, searching within a website, indexing by google(crawl), template+middleware in settings, track queries from mysql shell, Pagination in django | Score and counts customization + Merge Posts Functionality + Dashboard Review
25-30 April | concept of stopwords (very popular in ML), time complexity of "in" operator in python (for list, set, dict), time.perf_counter_ns(), jquery-plugin : (jquery-visible), timeout, ajax GET+POST | Similar Post Suggestion + Answer view count 
3-16 May | Django Rest Framework : Serializers (ModelSerializer) , APIView, Generic APIView (CreateAPIView), Basic familiarity with POSTMAN, Igmur(why it is used, and recent technologies which replaced it.)| Created API endpoint for question + answer creation with validation handling + Tool for posting question with preprocessing HTML contents. 
31 - 7 june | bootstrap push-pull class, auto_now vs auto_now_add vs default, submit button outside form, pagination, bootstrap table | Tag Merging suggestion by users + Tag Moderation from frontend 
8 - 9 june | Django+Mysql contains/exact filter is case insensitive by default ,Django messages revise | Mention a user in comments, watch option in moderation form, restriction while changing username
10-12 june | **Very Very Interesting :** How google search works [crawling + indexing], Google search console, benefit of sitemaps, robots.txt, django-sitemap-framework : Sitemap class, GenericSitemap, ping_google, limit, django-sites-framework(little bit), sitemap_index.xml, sitemap files, static vs dynamic sitemap. Important urls : [documentation-1](https://docs.djangoproject.com/en/1.11/_modules/django/contrib/sitemaps/#Sitemap) [documentation-2](https://docs.djangoproject.com/en/3.2/ref/contrib/sitemaps/#module-django.contrib.sitemaps) [sitemaps + robots.txt section](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap) | Create sitemaps and ping to google using cronjob
13-15 june| Google's **Programmable Search Engine or Custom search engine by google** : [1.](https://programmablesearchengine.google.com/cse/all) Insert some block of code in your html, to get search bar and the result in your site, or share public URL [2.](https://developers.google.com/custom-search/v1/introduction#identify_your_application_to_google_with_api_key) They provide an API endpoint to get json response, 100 search query per day free and paid for more queries per day with a limit of 10k queries per day. [3.](https://stackoverflow.com/a/22703153/14264497) Scraping is illegal, also google will detect and block. Finally, 100 was not enough for us, so stay with Ques10 internal suggest-post functionality. Another Point : Google cloud provides one API key, now you can use that key for various services of google like, Gmail API, Blogger API,  all the analytics will be maintained in seperate sections . BUT API key is one.|Play around with **Proggrammable search engine** to Suggest Post in ques10-assistant,  Read CSV file, remove stopwords, and write to CSV again
16-19 june |What is the correct way of returning json response for APIs | Ques10 Assistant Backend design using DRF, unique usernames
20-24 june | Get to know about the **Google Analytics** Interface, What data they are tracking (Real Time :D). Account>Property>Views in GA. We were using **Universal Analytics** which is old, now the updated one is **Google Analytics 4**. [Got to know about](https://support.google.com/analytics/answer/1033068?hl=en#zippy=%2Cin-this-article) and used Event Categories, Event Label, Event Value. [API](https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide#using-a-proxy-server) to send hit to **Universal Analytics** + Custom Django Management Commands : add_argument() actions, i used store_true | Send KPI Stats to **Google Analytics** using Events, created a model for KPI stats, refactored it completely.
28 june - 1 july | Holiday | Holiday
2-3 july | | Rewards pop-up etc, plan cancelled
4-5 july | allauth signals for email-change & email-confirm, allauth email change method, | Immediate score to user on profile complete,email-phone verified using signals
July | | Transaction for Views, Instant Score + level update, Lot of Scripts for Tag management 
