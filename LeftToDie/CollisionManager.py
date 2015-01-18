def checkCollision(player, tiles):
    for tile in tiles:
        # Don't care if it's empty
        if tile.name = "Empty":
            continue

        if player.boundingRect.colliderect(tile.boundingRect):
            if tile.name = "Spike":
                # DEATH DROP STATE EXECUTE
                pass
            elif tile.name = "End":
                # VICTORY LEAP STATE EXECUTE
                pass
            elif tile.name = "Block":
                # Reposition the block

                # Finds center points of the boundingRects
                playerPos = player.boundingRect.center
                tilePos = player.boundingRect.center

                # Finds diff vector between player and tile
                diff = (playerPos[0]-tilePos[0], playerPos[1]-tilePos[1])
                
                # If x is larger than the y, then we know that it is a horizontal collision
                if abs(diff[0]) > abs(diff[1]):
                    # If x is positive, then we reset player on the right of the tile
                    if  diff[0] > 0:
                        player.boundingRect.left = tile.boundingRect.right
                    # Else if negative, we set the player left of the tile
                    else:
                        player.boundingRect.right = tile.boundingRect.left

                # If y is larger than x, then there is a vertical collision
                else:
                    # If y is negative, then reset player on the top of the tile
                    # Note that this is opposite of x calclations because we have to keep
                    # in mind that y is reversed according to top left coordinates
                    if diff[1] < 0:
                        player.boundingRect.bottom = tile.boundingRect.top
                    else:
                        player.boundingRect.top = tile.boundingRect.bottom
                return
