import { useState, useEffect } from "react";

export interface CartItem {
  id_produit: number;
  nom_produit: string;
  prix_unitaire: number;
  quantite: number;
  type_produit?: string;
}

export function useCart() {
  const [cart, setCart] = useState<CartItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  // Load cart from localStorage on mount
  useEffect(() => {
    const storedCart = localStorage.getItem("mokpokpo_cart");
    if (storedCart) {
      try {
        setCart(JSON.parse(storedCart));
      } catch (error) {
        console.error("Failed to parse cart:", error);
      }
    }
    setIsLoading(false);
  }, []);

  // Save cart to localStorage whenever it changes
  useEffect(() => {
    if (!isLoading) {
      localStorage.setItem("mokpokpo_cart", JSON.stringify(cart));
    }
  }, [cart, isLoading]);

  const addToCart = (product: Omit<CartItem, "quantite">, quantity: number = 1) => {
    setCart((prevCart) => {
      const existingItem = prevCart.find((item) => item.id_produit === product.id_produit);
      
      if (existingItem) {
        return prevCart.map((item) =>
          item.id_produit === product.id_produit
            ? { ...item, quantite: item.quantite + quantity }
            : item
        );
      } else {
        return [...prevCart, { ...product, quantite: quantity }];
      }
    });
  };

  const removeFromCart = (id_produit: number) => {
    setCart((prevCart) => prevCart.filter((item) => item.id_produit !== id_produit));
  };

  const updateQuantity = (id_produit: number, quantite: number) => {
    if (quantite <= 0) {
      removeFromCart(id_produit);
      return;
    }
    
    setCart((prevCart) =>
      prevCart.map((item) =>
        item.id_produit === id_produit ? { ...item, quantite } : item
      )
    );
  };

  const clearCart = () => {
    setCart([]);
  };

  const getTotal = () => {
    return cart.reduce((total, item) => total + item.prix_unitaire * item.quantite, 0);
  };

  const getItemCount = () => {
    return cart.reduce((count, item) => count + item.quantite, 0);
  };

  return {
    cart,
    isLoading,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    getTotal,
    getItemCount,
  };
}
