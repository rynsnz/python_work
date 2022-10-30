"""
Establish a list of intersections in Chicago where the most red-light-camera
violations cited so far this year - pulled in from a notebook for demo...
"""
intersections = ['LAKE SHORE DR AND BELMONT',
 'LAFAYETTE AND 87TH',
 'CICERO AND I55',
 'WENTWORTH AND GARFIELD',
 'STONY ISLAND/CORNELL AND 67TH',
 'STATE AND 79TH',
 '99TH AND HALSTED',
 '75TH AND STATE',
 'HOLLYWOOD AND SHERIDAN',
 'STONEY ISLAND AND 76TH']

# write a for loop to print each intersection
print("Top 10 intersections in Chicago for Red Light Camera violations this year:")
for intersection in intersections: print(intersection)
print(f"\n #1 intersection: {intersections[0:1]}")