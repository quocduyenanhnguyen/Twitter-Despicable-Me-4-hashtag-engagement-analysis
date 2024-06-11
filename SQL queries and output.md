```use annaclinic1;```
### We will collect data from Jun 2, 2024 to Jun 8, 2024

#### Total number of posts
```select count(distinct Post_link) as post_count from Twitter_Despicable_Me_4_hashtag_engagement;```
#### Output
![Screen Shot 2024-06-11 at 11 41 53 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/6fe31039-a429-4f6f-ba5b-76ef08a22764)

-> There are 233 posts created within one week period for Despicable Me 4 hashtag

#### 1. average likes per post
```select round(avg(number_of_likes), 2) as average_likes_per_post from Twitter_Despicable_Me_4_hashtag_engagement;```
#### Output
![Screen Shot 2024-06-11 at 11 44 29 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/930b794c-02b4-4009-adb6-e207a8012393)

-> On average, we have nearly 65 likes per post 

#### 2. average comments per post
```select round(avg(number_of_comments), 2) as average_comments_per_post from Twitter_Despicable_Me_4_hashtag_engagement;```
#### Output 
![Screen Shot 2024-06-11 at 11 45 34 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/becc2e3d-e321-487f-acd1-60a1a6c12c31)

-> On average, we have about 1.6 comments per post

#### 3. total engagement (sum of likes, comments, and shares)
#### Sum of likes
```select sum(number_of_likes) as sum_of_likes from Twitter_Despicable_Me_4_hashtag_engagement;```
#### Output
![Screen Shot 2024-06-11 at 11 46 24 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/fc4cf8aa-c558-4600-871d-744f97a3cfee)

-> We have 15129 likes in total

#### Sum of comments
```select sum(number_of_comments) as sum_of_comments from Twitter_Despicable_Me_4_hashtag_engagement;```
#### Output
![Screen Shot 2024-06-11 at 11 47 06 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/0257d4d1-830b-4020-a014-f3062c997341)

-> We have 363 comments in total

#### 4. Identify any patterns or trends (such as peak posting times or most engaging content types)
#### Let's look at top 3 sort by view count in descending order
```select Post_link, Date_posted, Content_type, Content_format, View_count from Twitter_Despicable_Me_4_hashtag_engagement order by View_count desc;```
#### Output
![Screen Shot 2024-06-11 at 11 49 18 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/5c484130-4910-437a-9c50-533973cc6462)

#### Now, let's look at top 3 sort by number of likes in descending order
```select Post_link, Date_posted, Content_type, Content_format, View_count from Twitter_Despicable_Me_4_hashtag_engagement order by number_of_likes desc;```
#### Output
![Screen Shot 2024-06-11 at 11 49 59 AM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/bd19a6a5-0942-49fb-8440-589b37927c9f)

-> Look at the top 3 in both cases, we see that most people click to view short clips from this upcoming movie, or click on gaming-related contents 
(because everyone loves playing game(?!)). Also, it is worth noting that contents that fall under Announcement type in picture and video formats have the 
most likes and view count as well while once in awhile, they may view contents that are about Express thoughts but not as much as Announcement theme.

#### Let's add clarity for some Content Types:
#### Announcement: 
Broad term that includes anything related to making something known publicly, whether it's related to releasing new trailers or a short clip is released, etc. 
Personal opinions and statement of truth may be included but if the content leans more towards Announcement theme, then it will be labeled Announcement.

#### Express thoughts: 
Personal opinions, thoughts, feelings, emotions that are visible from reading the text right off the bat.

#### Let's take a closer look at number of likes, comments, quotes, reposts, and view count, and check their correlation
#### View Count and number of likes 
```
select @ax := avg(View_Count), 
       @ay := avg(Number_of_likes), 
       @div := (stddev_samp(View_Count) * stddev_samp(Number_of_likes))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((View_Count - @ax) * (Number_of_likes - @ay) )/((count(View_Count) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 00 33 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/1e3322d5-1f76-4f58-a7e7-6a922858293f)

-> They have a moderate relationship

#### View Count and number of comments
```
select @ax := avg(View_Count), 
       @ay := avg(Number_of_comments), 
       @div := (stddev_samp(View_Count) * stddev_samp(Number_of_comments))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((View_Count - @ax) * (Number_of_comments - @ay) )/((count(View_Count) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 02 17 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/c93b17e9-2901-4d1a-8706-07b510c52f1d)

-> They also have a moderate relationship

#### View Count and number of quotes
```
select @ax := avg(View_Count), 
       @ay := avg(Number_of_quotes), 
       @div := (stddev_samp(View_Count) * stddev_samp(Number_of_quotes))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((View_Count - @ax) * (Number_of_quotes - @ay) )/((count(View_Count) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 02 59 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/26380122-70b9-4a94-ab65-9ce09e89a305)

-> They have a a moderate relationship

#### View Count and number of reposts
```
select @ax := avg(View_Count), 
       @ay := avg(Number_of_reposts), 
       @div := (stddev_samp(View_Count) * stddev_samp(Number_of_reposts))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((View_Count - @ax) * (Number_of_reposts - @ay) )/((count(View_Count) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 03 34 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/4529fbd4-51cf-4c36-9c16-d15e351e2958)

-> They have a moderate relationship

#### Let's look closely at number of likes, comments, quotes, reposts, and check their correlation with number of likes 
#### (because liking a post is the first thing that people do when they view a post that they enjoy so we are curious to see if it's related to other metrics)
#### Number of likes and number of comments
```
select @ax := avg(Number_of_likes), 
       @ay := avg(Number_of_comments), 
       @div := (stddev_samp(Number_of_likes) * stddev_samp(Number_of_comments))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((Number_of_likes - @ax) * (Number_of_comments - @ay) )/((count(Number_of_likes) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 04 55 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/1069b57c-004a-454c-986b-84bc929b113c)

-> They have a moderate relationship

#### Number of likes and number of quotes
```
select @ax := avg(Number_of_likes), 
       @ay := avg(Number_of_quotes), 
       @div := (stddev_samp(Number_of_likes) * stddev_samp(Number_of_quotes))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((Number_of_likes - @ax) * (Number_of_quotes - @ay) )/((count(Number_of_likes) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 05 27 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/9c937f38-4505-4f06-a87a-8fb41b4278de)

-> They have a moderate relationship

#### Number of likes and number of reposts
```
select @ax := avg(Number_of_likes), 
       @ay := avg(Number_of_reposts), 
       @div := (stddev_samp(Number_of_likes) * stddev_samp(Number_of_reposts))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((Number_of_likes - @ax) * (Number_of_reposts - @ay) )/((count(Number_of_likes) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 05 58 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/3260ed13-2a52-43e4-9746-16768fb820e9)

-> They have a strong relationship

-> In conclusion, most of them have moderate relationship with View Count and Number of Likes but the correlation is the strongest between Number of Likes and number of reposts

#### Let's find out how many posts per specific time of the day
#### Hours posted
```
select date_format(date_posted, '%H') as hours_posted, count(distinct post_link) as count
from Twitter_Despicable_Me_4_hashtag_engagement group by date_format(date_posted, '%H')
order by count desc;
```

#### Output
![Screen Shot 2024-06-11 at 12 08 59 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/e4faa309-ed2d-4a8f-823c-5e71677726c8)

-> Most users posted at 9:00 AM, 4:00 PM, and 6:00 AM PST.

#### Hours and date posted
```
select date_format(date_posted, '%Y-%m-%d') as date_posted, date_format(date_posted, '%H') as hours_posted, count(distinct post_link) as count
from Twitter_Despicable_Me_4_hashtag_engagement group by date_format(date_posted, '%Y-%m-%d'), date_format(date_posted, '%H')
order by count desc;
```

#### Output
![Screen Shot 2024-06-11 at 12 10 51 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/0ec1d33c-717c-4df5-be83-4d1586a3a39a)

-> Most users posted at 6:00 AM, 9:00 AM, and 10:00 PM PST on Jun 5 and Jun 6.

#### date posted
```
select date_format(date_posted, '%Y-%m-%d') as date_posted, count(distinct post_link) as count
from Twitter_Despicable_Me_4_hashtag_engagement group by date_format(date_posted, '%Y-%m-%d')
order by count desc;
```

#### Output
![Screen Shot 2024-06-11 at 12 12 00 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/3459caba-8bd4-4bb0-b294-785518218f3f)

-> Most users posted on Jun 5 and Jun 7.

#### let's look at posting time and see its correlation with Number of Likes, Comments
#### Posting time and Number of Likes
```
select @ax := avg(date_posted), 
       @ay := avg(Number_of_Likes), 
       @div := (stddev_samp(date_posted) * stddev_samp(Number_of_Likes))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((date_posted - @ax) * (Number_of_Likes - @ay) )/((count(date_posted) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 13 12 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/4859b895-4060-49bf-a252-ae9951cfeeea)

-> No relationship

#### Posting time and Number of Comments
```
select @ax := avg(date_posted), 
       @ay := avg(Number_of_comments), 
       @div := (stddev_samp(date_posted) * stddev_samp(Number_of_comments))
from Twitter_Despicable_Me_4_hashtag_engagement;

select sum((date_posted - @ax) * (Number_of_comments - @ay) )/((count(date_posted) -1) * @div) as correlation
from Twitter_Despicable_Me_4_hashtag_engagement;
```

#### Output
![Screen Shot 2024-06-11 at 12 13 54 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/20d2b4aa-7484-4620-a896-6458d2ca8cc2)

-> No relationship

#### let's look at relationship between content type and number of likes, comments
```
select distinct content_type, count(distinct post_link) as posts_count, sum(number_of_likes) as total_likes, 
sum(number_of_comments) as total_comments
from Twitter_Despicable_Me_4_hashtag_engagement group by content_type;
```

#### Output
![Screen Shot 2024-06-11 at 12 15 03 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/1ccf7a53-1f01-4eec-81c8-5346d036be72)

-> Express thoughts, Announcement, and No text have more posts, total likes, and total comments than other content type.

#### let's look at relationship between content format and number of likes, comments
```
select distinct content_format, count(distinct post_link) as posts_count, sum(number_of_likes) as total_likes, 
sum(number_of_comments) as total_comments
from Twitter_Despicable_Me_4_hashtag_engagement group by content_format;
```

#### Output
![Screen Shot 2024-06-11 at 12 15 48 PM](https://github.com/quocduyenanhnguyen/Twitter-Despicable-Me-4-hashtag-engagement-analysis/assets/92205707/a60e0752-54fc-4cc6-b0fa-61aa640fdf7f)

-> Picture, video, GIF image, and text combination have more posts, total likes, and total comments than other content format.


