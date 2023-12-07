from functools import reduce as r

class SeedTransformer:
    def __init__(self, seeds, mappings):
        self.seeds = seeds
        self.mappings = mappings

    def apply_mapping(self, start, length, mapping):
        for m in mapping.split('\n')[1:]:
            dest, src, size = map(int, m.split())
            delta = start - src
            if delta in range(size):
                size = min(size - delta, length)
                return (dest + delta, size)
        return start, length

    def transform_seed(self, seed):
        start, length = seed
        transformed_seed = []
        while length > 0:
            transformed = self.apply_mapping(start, length, self.mappings)
            transformed_seed.append(transformed)
            start, length = transformed
        return min(transformed_seed)

    def get_transformed_results(self):
        seed_sets = [
            [self.seeds, [1] * len(self.seeds)],
            [self.seeds[0::2], self.seeds[1::2]]
        ]
        return [min(r(self.transform_seed, seed_set))[0] for seed_set in seed_sets]

def transform_seeds(seeds, mappings):
    seed_transformer = SeedTransformer(seeds, mappings)
    return seed_transformer.get_transformed_results()

# Access and read the data from the 'input.txt' file
with open('input.txt') as file:
    content = file.read().split('\n\n')

# Extract seed values and mappings from the content
seeds = list(map(int, content[0].split()[1:]))
mappings = content[1]

# Calculate the minimum value for each set of seeds and print the result
results = transform_seeds(seeds, mappings)
print(*results)
