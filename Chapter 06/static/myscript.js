function myfunction(id)
{
  var nm=document.getElementById("nmId").value;
  var btn=document.getElementById(id).name;
  if (btn=="button1")
  {
    alert(nm+", Of Course You Can Vote! Cheers");
  }
  else
  {
    alert("No Voting Rights For You Yet,"+nm+"! (:");
  }
}
