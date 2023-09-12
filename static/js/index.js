index = 1

function convert_from_textbox(){
    text = document.getElementById('main-textarea').value;
    if (text===''){
        document.getElementById('err-msg').innerHTML = 'Your text field is blank.'
        return
    }
    fetch('/convert/text', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({text})
    })
    .then(response => response.blob())
    .then(data=>{
        document.getElementById('err-msg').innerHTML = ''
        saveAs(data, 'data.csv')
    });
};

function convert_from_url(){
    var url_boxes = document.getElementsByName('urlbox');
    var urls = []
    console.log(url_boxes)
    url_boxes.forEach(element=>{
        if (element.value !== ''){
            urls.push(element.value);
        }
    })
    console.log(urls)
    if (urls.length == 0){
        document.getElementById('err-msg').innerHTML = 'Please add at least one link.'
        return
    }
    fetch('/convert/url', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({urls})
    })
    .then(response => response.blob())
    .then(data=>{
        document.getElementById('err-msg').innerHTML = ''
        saveAs(data, 'data.csv')
    })
};

function add_url_box(){
    var urlbox_container = document.getElementById('urlbox-container');
    var new_box = document.createElement('div');
    new_box.setAttribute('class', 'urlbox-wrapper mb-2 row w-100 gx-1');
    new_box.setAttribute('id', `urlbox-${index}`)
    new_box.innerHTML = `
        <div class="px-1 col-sm-11" >
            <input type="text" name="urlbox" class="px-2 w-100 h-100 mb-2 mb-sm-0" placeholder="Paste the link here...">
        </div>
        <div class="px-1 col-sm-1">
            <button onclick="remove_url_box(${index})" class="btn btn-outline-dark w-100">X</button>
        </div>`;
    urlbox_container.append(new_box)
    index += 1
}

function remove_url_box(index){
    document.getElementById(`urlbox-${index}`).remove();
}