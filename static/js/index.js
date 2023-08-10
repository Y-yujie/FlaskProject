var imageID = null

function ProcessFile(e) {
    var file = document.getElementById('file').files[0];  // files集合中包含一组File对象，files[0]本地文件系统中的文件名
    if (file) {  // 可显示多张图片
        var reader = new FileReader();  // 用于图片预览对象
        var ctx = document.getElementById('canvas').getContext('2d');
        var img = new Image();


        // 显示预测结果
        var fileName = file.name;
        var index = fileName.lastIndexOf('.');  // 获取.最后一次出现的索引
        imageID = fileName.substring(0, index);

        reader.onload = function (event) {  // 处理load事件。该事件在读取操作完成时触发
            img.onload = function () {
                ctx.drawImage(img, 0, 0, 300, 300)
            }
            var txt = event.target.result;  // 通过result属性拿到图片的Base64格式的数据
            img.src = txt; // 将图片base64字符串赋值给img的src
        };
    }
    reader.readAsDataURL(file);  // 将file(图片)转换为base64码
}

$(document).ready(function () {
    // Function to display the data in a container
    function displayData(data, containerId) {
        var container = $(containerId);
        container.empty();

        if (data) {
            var html = "<ul>";
            data.forEach(function (row) {
                html += "<li>" + row.numbers + "</li>";
            });
            html += "</ul>";
            container.html(html);
        } else {
            container.html("Data not found.");
        }
    }

    // Event handler for the "file" button
    $("#acquire").click(function () {
        var dataToSend = {
            customVariable: imageID
        };

        $.ajax({
            type: "POST",
            url: "/auth/search_data",
            data: JSON.stringify(dataToSend),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                console.log(response);
                displayData(response, "#searchResultContainer");
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });
    // predictShow.textContent += title;
});

function contentloaded() {
    document.getElementById('file').addEventListener('change', ProcessFile, false);
}

window.addEventListener('DOMContentLoaded', contentloaded, false); // DOM渲染完即可执行，此时图片视频可能还没加载完