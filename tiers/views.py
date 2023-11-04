from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .forms import TierItemForm
from .models import TierItem, TierList, TierRow


@require_GET
def index(request):
    return render(
        request,
        "index.html",
        {
            "tierlists": TierList.objects.all(),
        },
    )


@require_GET
def details(request, pk):
    tierlist = TierList.objects.get(id=pk)
    form = TierItemForm()
    return render(
        request,
        "details.html",
        {
            "form": form,
            "tier_items": TierItem.objects.filter(
                tierlist_id=tierlist.id, tierrow=None
            ),
            "tierlist": tierlist,
        },
    )


@require_POST
def upload_image(request, pk):
    form = TierItemForm(request.POST, request.FILES)
    if form.is_valid():
        tierlist = TierList.objects.get(id=pk)
        form.instance.tierlist = tierlist
        form.save()
    response = render(
        request,
        "components/tier_item.html",
        {"tier_item": form.instance},
        status=201,
    )
    return response


@require_POST
def dropped(request):
    try:
        tier_row_id = int(request.POST["tier_row_id"].lstrip("tr-"))
    except Exception:
        tier_row_id = None

    tier_item_id = int(request.POST["tier_item_id"].lstrip("ti-"))

    # Save TierItem to TierRow
    tier_row = TierRow.objects.get(id=tier_row_id) if tier_row_id else None
    tier_item = TierItem.objects.get(id=tier_item_id)

    if tier_item.tierrow_id is None:
        # TierItem not already assigned
        tier_item.tierrow = tier_row
        tier_item.save()
    elif tier_row_id is None:
        # Moving back to tier_row
        tier_item.tierrow = None
        tier_item.save()
    elif tier_item.tierrow_id == tier_row_id:
        # Item already assigned to current TierRow. Make no changes
        return HttpResponse(status=201)
    else:
        # Item assigned to something else, move it
        # old_id = tier_item.tier_row_id
        tier_item.tierrow = tier_row
        tier_item.save()

    return render(
        request,
        "components/swap-tier-items-base.html",
        {"tier_item": tier_item},
        status=201,
    )


def delete_tier_item(request, pk):
    TierItem.objects.get(id=pk).delete()
    return HttpResponse(status=200)
