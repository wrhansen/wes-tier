from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .forms import TierItemForm
from .models import TierItem, TierList, TierRow


@require_GET
def index(request):
    tierlist = TierList.objects.create_list_and_rows()
    form = TierItemForm()
    return render(
        request,
        "index.html",
        {
            "form": form,
            "tier_items": TierItem.objects.filter(
                tierlist_id=tierlist.id, tierrow=None
            ),
            "tierlist": tierlist,
        },
    )


@require_POST
def upload_image(request):
    form = TierItemForm(request.POST, request.FILES)
    if form.is_valid():
        tierlist = TierList.objects.get(id=1)
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
def move_to_tier(request, from_tier, to_tier):
    pass


@require_POST
def dropped(request):
    print(request.POST)
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