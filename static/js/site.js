function allowDrop(ev) {
    ev.preventDefault();
}

function onDrag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function onDrop(ev) {
    data = ev.dataTransfer.getData("text");
    target = ev.target.closest("div.tier_row");
    target.setAttribute("hx-vals", JSON.stringify({
        "tier_item_id": data
    }));
}
