
function changeState(){
    document.getElementById("modaltitle1").innerHTML='新增用户';
    document.getElementById("InputName").value="";
    document.getElementById("InputID").value="";
    document.getElementById("InputClass").value="";
    document.getElementById("InputTel").value="";
    document.getElementById("hidden1").value=0;
}

function readytoPut(id){
     $.ajax({
        url:'',
        type:'GET',
        contentType:"application/json;charset=utf-8;",
        dataType:"text",
        data:{'id':id},
        success:function(responds){
            var responds = JSON.parse(responds); 
            document.getElementById("InputName").value=responds['Name'];
            document.getElementById("InputID").value=responds['Username'];
            document.getElementById("InputClass").value=responds['Class'];
            document.getElementById("InputTel").value=responds['Tel'];
            document.getElementById("hidden1").value=responds['ID']
            document.getElementById("modaltitle1").innerHTML='更改信息';
        },
    })
}
function submit2(){
    toastr.options = {
                positionClass: "toast-top-center",   
            };
    InputName=document.getElementById("InputName1").value;
    InputID=document.getElementById("InputID1").value;
    InputClass=document.getElementById("InputClass1").value;
    InputTel=document.getElementById("InputTel1").value;
    var regex=new RegExp(/^[0-9]+$/)
    if(InputName=="" ||InputID==""){
        alert("姓名,账号不能为空！");
        return;
    }
    if(InputTel!="" && regex.test(InputTel)==0){
        alert("只能输入数字组成的电话号码");
        return;
    }
    var flag=confirm("确定要提交该信息吗？提交后将无法修改。");
    if(flag==0)return;
    $.ajax({
        url:'',
        type:'POST',
        contentType:"application/x-www-form-urlencoded;charset=utf-8;",
        dataType:"text",
        data:{'Name':InputName,'Username':InputID,'Class':InputClass,'Tel':InputTel},
        error:function(){
        toastr.error("提交失败!");
            
        },
        success:function(){
            toastr.success("你已成功提交!");
            document.getElementById("InputID1").value="";
            document.getElementById("InputName1").value="";
            document.getElementById("InputClass1").value="";
            document.getElementById("InputTel1").value="";
            document.getElementById("hidden11").value=0;
            setTimeout("window.location.reload()",500)
        }
    }) }
function submit1(){
    toastr.options = {
                positionClass: "toast-top-center",   
            };
    InputName=document.getElementById("InputName").value;
    InputID=document.getElementById("InputID").value;
    InputClass=document.getElementById("InputClass").value;
    InputTel=document.getElementById("InputTel").value;
    hidden1=document.getElementById("hidden1").value;
    var regex=new RegExp(/^[0-9]+$/)
    if(InputName=="" ||InputID==""){
        alert("姓名,账号不能为空！");
        return;
    }
    if(InputTel!="" && regex.test(InputTel)==0){
        alert("只能输入数字组成的电话号码");
        return;
    }

    $.ajax({
        url:'',
        type:'POST',
        contentType:"application/x-www-form-urlencoded;charset=utf-8;",
        dataType:"text",
        data:{'Name':InputName,'Username':InputID,'Class':InputClass,'Tel':InputTel,'id':hidden1},
        error:function(){
            if(hidden1==0){
                toastr.error("提交失败!");
            }
            else{ 
                toastr.error("修改失败")
            }
        },
        success:function(){
            if(hidden1==0){
                toastr.success("你已成功提交!");
            }
            else{
                toastr.success("修改成功");
            }
            document.getElementById("InputID").value="";
            document.getElementById("InputName").value="";
            document.getElementById("InputClass").value="";
            document.getElementById("InputTel").value="";
            document.getElementById("hidden1").value=0;
            setTimeout("window.location.reload()",500)
        }
    }) }
function Delete(id){
    toastr.options = {
                positionClass: "toast-top-center",   
            };
    var flag=confirm("确定要删除该条信息吗？");
    if(flag==0)return;
   $.ajax({
    url:'',
    type:'POST',
    contentType:"application/x-www-form-urlencoded;charset=utf-8;",
    dataType:"text",
    data:{'id':id},
    error:function(){
        toastr.error("删除失败");
    },
    success:function(){
        toastr.success("删除成功");
        console.log("ok")
        setTimeout("window.location.reload()",500)
    }
    }) 
}