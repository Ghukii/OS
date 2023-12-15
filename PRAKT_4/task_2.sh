echo "Текущий каталог: $(pwd)"

echo "Содержимое текущего каталога:"
ls

mkdir task_2_dir

chmod +w task_2_dir

touch task_2.txt
ln -s task_2.txt task_2_link

read -p "Введите команду для выполнения: " command
eval $command

chmod -w task_2_dir

exit 0
