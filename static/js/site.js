function allowDrop(ev) {
    ev.preventDefault();
}

function onDrag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function onDrop(ev) {
    data = ev.dataTransfer.getData("text");
    ev.target.setAttribute("hx-vals", JSON.stringify({
        "tier_item_id": data
    }));
}
