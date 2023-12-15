sizes=()

for directory in ~/?*/; do
    sizes+=("$directory $(du -sb "$directory" | cut -f1)")
done

echo "%s\t%s\n" "Directory" "Size" "${sizes[@]}" > dir_sizes.csv

cat dir_sizes.csv
