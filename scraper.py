# Rolimons limited item scraper

try:
    import rolimons
except ImportError:
    import os
    os.system("pip3 install rolimons")
    import rolimons

ids_to_scrape = [
    16744155285,
    13753760092,
    108147339,
] # Change these ids to limiteds from rolimons


save_info = True # True or False

class Scraper:
    @staticmethod
    def scrape():
        scraped_items = []
        for item_id in ids_to_scrape:
            try:
                item = rolimons.item(item_id)
                name = item.name
                owner_data = item.get_owner_data()
                owners = owner_data.owner_names
                owners_id = owner_data.owner_ids
                scraped_items.append(name)
                if save_info:
                    with open(f"{name}.txt", "w") as f:
                        f.write(name + '\n')
                        if owners_id:
                            for owner_id, owner in zip(owners_id, owners):
                                if owner:
                                    f.write(f"{owner_id}: {owner}\n")
                        else:
                            raise ValueError(f"No owners found for item: {name}")  
                else:
                    print(name)
                    if owners_id:
                        for owner_id, owner in zip(owners_id, owners):
                            if owner:
                                print(f"{owner_id}: {owner}")
                    else:
                        print(f"No owners found for item: {name}")
            except Exception as e:
                pass
        return scraped_items



print(Scraper().scrape())
