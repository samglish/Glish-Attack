!/bin/bash

read -p "Selectionnez une option (1, 2 ou 3) : " option
# Remplacez par la valeur que vous voulez tester

case $option in
    1)
        echo "Option 1 sélectionnée."
        ;;
    2)
        echo "Option 2 sélectionnée."
        ;;
    3)
        echo "Option 3 sélectionnée."
        ;;
    *)
        echo "Option non reconnue."
        ;;
esac
