from django.shortcuts import render, redirect
from .forms import PlaceForm
import random
from django.http import JsonResponse

# Create your views here.
def index(request):

    return render(request, 'index.html')

def places_list(request):
    places = get_places_from_session(request)
    return render(request, 'places_list.html', {"places": places})

def place_detail(request, pk):
    places = get_places_from_session(request)
    place = places.get(str(pk))
    return render(request, "place_detail.html", {"place": place})

def add_place(request):
    places = get_places_from_session(request)
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            new_id = int(max(places.keys())) + 1 if places else 1
            places[str(new_id)] = {
                "id": new_id,
                "name": form.cleaned_data["name"],
                "description": form.cleaned_data["description"],
                "location": form.cleaned_data["location"],
                "rating": form.cleaned_data["rating"],
                "image": "img/default.jpg",
            }
            request.session["places"] = places
            return redirect("places:places_list")
    else:
        form = PlaceForm()

    return render(request, "add_place.html", {"form": form})

def random_place_json(request):
    places = get_places_from_session(request)
    if not places:
        return JsonResponse({"error": "No places found"}, status=404)

    place_list = list(places.values())
    weights = [place["rating"] for place in place_list]
    chosen_place = random.choices(place_list, weights=weights, k=1)[0]

    return JsonResponse(chosen_place)

def get_places_from_session(request):
    if "places" not in request.session:
        print("Creating new session")
        request.session["places"] = {}
    return request.session["places"]