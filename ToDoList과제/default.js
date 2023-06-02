var toDoList= new Array();
// get input and save it into list
function addList(){
    var results = document.getElementById('finalResult');
    var newone= document.getElementById('list').value;
    var item = document.createElement('li');
    //no input
    if(newone==''){
        alert("Add something!");
    }
    else{
       //add todo list
        item.textContent = newone;
        item.classList.add('list-group-item','list-group-item-secondary',"form-check");
        
        results.appendChild(item);
        toDoList.push(newone);
        console.log(toDoList);
        // add remove button 
        var removebtn = document.createElement('button');
        removebtn.innerText = 'Remove';
        removebtn.classList.add('btn', 'btn-outline-danger');
        removebtn.addEventListener('click', removeList);
        item.appendChild(removebtn);
                        
    }
}
//remove specific element from the list
function removeList(){
    var results= document.getElementById('finalResult');
    results.removeChild(this.parentNode);
//    remove element in todoList by index
    var idx = toDoList.indexOf(this.parentElement.innerText.split("Remove")[0])
    toDoList.splice(idx,1);
    console.log(toDoList);
}
//clear all
function clearList(){
    var results=document.getElementById('finalResult');
    results.innerHTML='';
    toDoList =[];
    console.log(toDoList);
}