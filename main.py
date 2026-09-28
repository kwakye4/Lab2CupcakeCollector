import pygame
import asyncio # 1. Import asyncio

async def main(): # 2. Wrap everything in an async main function
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Your game logic and drawing goes here
        screen.fill((0, 0, 0))
        pygame.display.flip()

        await asyncio.sleep(0) # 3. VERY IMPORTANT: Yield control to the browser

# 4. Run the async main function
asyncio.run(main())
