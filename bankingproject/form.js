
var branchesKollam=["Umayanalloor", "Pallimukku", "Kottiyam"];
var branchesThiruvananthapuram=["Attingal", "Kallambalam", "Thampannoor"];
var branchesErnakulam=["Kakkanad", "Edapally", "Kaloor"];
var branchesThrissur=["Chalakkudi", "Athirappally", "Iranjalikkuda"];
var branchesKottayam=["Pala", "Eerattupetta", "Ettumanoor"];


function districtChanged(district)
{
var selectBranch = document.getElementById('branches');
var ln = selectBranch.length - 1;
while (ln > 0)
{
selectBranch.remove(1); //Remove all but "Select State"
ln--;
}



var branchArray;

switch(district)
{
case "Kollam":
branchArray=branchesKollam
break;
case "Thiruvananthapuram":
branchArray=branchesThiruvananthapuram
break;
case "Ernakulam":
branchArray=branchesErnakulam
break;
case "Thrissur":
branchArray=branchesThrissur
break;
case "Kottayam":
branchArray=branchesKottayam
break;
default:
}

for (i = 0; i < branchArray.length; i++)
{
var option = document.createElement('option');
option.text = branchArray[i];
option.value = branchArray[i];
selectBranch.add(option);
}

}

