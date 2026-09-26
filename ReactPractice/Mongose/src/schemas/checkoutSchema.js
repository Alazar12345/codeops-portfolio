import { z } from "zod";


export const checkoutSchema = z.object({

  name: z
    .string()
    .min(3, "Name must be at least 3 characters"),


  phone: z
    .string()
    .min(10, "Enter a valid phone number"),


  address: z
    .string()
    .min(5, "Address is required"),


  payment: z
    .string()
    .min(1, "Select payment method"),

});
