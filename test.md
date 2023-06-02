물론입니다! 파이썬으로 버블 정렬 알고리즘을 구현해보겠습니다.

[google](https://www.google.com)

```python
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # 리스트를 한 번 순회하며 큰 값들을 맨 뒤로 보냄
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# 정렬하고자 하는 리스트
my_list = [5, 2, 8, 1, 9, 3]
print("정렬 전:", my_list)

sorted_list = bubble_sort(my_list)
print("정렬 후:", sorted_list)
```

위의 코드는 입력된 리스트를 버블 정렬 알고리즘을 사용하여 오름차순으로 정렬합니다. 

먼저 `bubble_sort` 함수를 정의합니다. 이 함수는 입력된 리스트 `arr`을 받아서 버블 정렬을 수행한 후 정렬된 리스트를 반환합니다.

알고리즘의 핵심은 두 번의 반복문을 사용하는 것입니다. 외부 반복문은 리스트를 한 번씩 순회하며 큰 값들을 맨 뒤로 보냅니다. 내부 반복문은 현재 요소와 그 다음 요소를 비교하여 순서를 바꿉니다. 이렇게 반복문을 수행하면 가장 큰 값이 맨 뒤로 이동하게 되고, 정렬 범위를 줄여가며 반복하여 전체 리스트가 정렬됩니다.

위의 코드에서는 입력으로 `[5, 2, 8, 1, 9, 3]`을 사용하여 정렬을 수행하고, 정렬 전과 후의 리스트를 출력합니다. 결과는 `[1, 2, 3, 5, 8, 9]`가 됩니다.

이 코드를 실행하면 입력한 리스트가 오름차순으로 정렬된 결과를 확인할 수 있습니다.

다음은 이 페이지의 소스 코드 입니다.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>md viewer</title>
    
    <link href="/static/stylesheets/style.css" rel="stylesheet">
    <link href="/static/stylesheets/prism.css" rel="stylesheet" />
	<link href="/static/stylesheets/github-markdown.css" rel="stylesheet">

    <script src="/static/js/prism.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/4.6.1/socket.io.min.js"></script>
    <script src="https://cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js"></script>
    <script>
        function mdtohtml(row_text){
            const md = new Remarkable();
            return md.render(row_text);
        }
    </script>
</head>
<body>
    <script>
        document.addEventListener("DOMContentLoaded", function(){
            var sock = io.connect('http://127.0.0.1:5000');
            sock.on('message', function(msg){
                if(msg.type === 'assistant'){
                    if (msg.status === 'running'){
                        $('.markdown-body').last().html(mdtohtml(msg.md));
                    }
                    else if (msg.status === 'start'){
                        $('#chatList').append('<div class="chatting-card"><div class="markdown-body">'+ mdtohtml(msg.md) + '</div></div>');
                    }
                    $(".markdown-body").last().find("code").each(function(index, item) {
                        Prism.highlightElement(item);
                    });
                    $(".markdown-body").last().find("code").removeClass('language-none');
                }else{
                    $('#chatList').append('<div class="markdown-body">'+ mdtohtml(msg.md) + '</div>');
                }
                console.log('Received Message : '+ msg.type);
            });
        });
    </script>
    <div id="chatList">
        {% for html in Cache %}
            <div class="chatting-card">
                <div class="markdown-body">
                    {{html|safe}}
                </div>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

> # Hello World
> 이것은 인용구 입니다.
>> 하하하하