var toDoList= new Array();
// get input and save it into list
function addList(){
    var results = document.getElementById('finalResult');
    var newone= document.getElementById('list').value;
    var item = document.createElement('li');
    //no input
    if(newone==''){
        alert("Add todo list");
    }
    else{
       
        item.textContent = newone;
        item.classList.add('list-group-item','list-group-item-secondary',"form-check");
        
        results.appendChild(item);
        toDoList.push(newone);
        // add remove button 
        var removebtn = document.createElement('button');
        removebtn.innerText = 'Remove';
        removebtn.classList.add('btn', 'btn-outline-danger');
        removebtn.addEventListener('click', removeList);
        item.appendChild(removebtn);
                        
    }

}

function removeList(){
    var results= document.getElementById('finalResult');
    var t = this.parentElement.innerText;
    results.removeChild(this.parentNode);
    console.log("before",toDoList)
    var idx = toDoList.indexOf(this.parentElement.innerText.split("Remove")[0])
    toDoList.splice(idx,1)
    console.log(toDoList)
}

function clearList(){
    var results=document.getElementById('finalResult');
    results.innerHTML='';
    toDoList =[];
}