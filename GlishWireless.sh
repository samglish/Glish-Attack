!/bin/bash

echo "*******************************************************************************"
echo "**                     APPLICATION DE BEIDI DINA SAMUEL                      **"
echo "**                        Ethical Hacking - Pentest                          **"
echo "*******************************************************************************"
echo "**                  https://github.com/samglish/Glish-Attack                 **"
echo "*******************************************************************************"
echo ""
echo "1. Wireless Show"
echo "2. Wireless Attack"
echo "3. Wireless Logout"

echo "4. Wireless Connect"
echo "5. My interface"
echo ""
echo "*******************************************************************************"

read -p "Selectionnez une option (1, 2 ou 3) : " option
# Remplacez par la valeur que vous voulez tester

case $option in
    1)
        echo "Wireless"
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
